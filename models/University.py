from enums.SudyField import StudyField
from models.Faculty import Faculty
from models.Student import Student
from tools.Tools import Tools
from util.FileManager import FileManager
from util.Logger import Logger


class University:
    def __init__(self):
        self.faculties = []
        self.scanner = input
        saved_faculties = FileManager.load_university_state()
        if saved_faculties:
            self.faculties.extend(saved_faculties)

    def find_faculty_by_criteria(self, criteria):
        return next((faculty for faculty in self.faculties if criteria(faculty)), None)

    def find_faculty_by_name(self, faculty_name):
        return self.find_faculty_by_criteria(lambda faculty: faculty.get_name() == faculty_name)

    def find_faculty_by_abbreviation(self, faculty_abbreviation):
        return self.find_faculty_by_criteria(lambda faculty: faculty.get_abbreviation() == faculty_abbreviation)

    def create_faculty(self):
        print("Please enter the input in the format: <faculty name>/<faculty abbreviation>/<field>")
        faculty_input = self.scanner()
        faculty_details = Tools.parse_input(faculty_input)
        faculty_name = faculty_details[0]
        faculty_abbreviation = faculty_details[1]
        field = faculty_details[2]

        try:
            study_field = StudyField[field.upper()]
            new_faculty = Faculty(faculty_name, faculty_abbreviation, [], study_field)
            self.faculties.append(new_faculty)
            Logger.log_faculty_creation(new_faculty)
            print("Faculty created successfully!")
        except KeyError:
            print(f"Invalid study field: {field}")

        self.save_university_state()

    def get_all_faculties(self):
        return self.faculties

    def search_student_faculty(self):
        print("Please enter the student email to search for their faculty")
        student_email = self.scanner()
        for faculty in self.faculties:
            for student in faculty.get_students():
                if student.get_email().lower() == student_email.lower():
                    print(f"Faculty {faculty.get_name()}")
                    return faculty
        print(f"Faculty not found for student with the email: {student_email}")
        return None

    def display_university_faculties(self):
        if not self.faculties:
            print("No faculties found in the university.")
        else:
            print("University Faculties:")
            for faculty in self.faculties:
                print(f"{faculty.get_name()} ({faculty.get_abbreviation()})")

    def display_faculties_by_field(self):
        print("Please enter the field name to filter faculties")
        field_input = self.scanner()
        try:
            field = StudyField[field_input.upper()]
            print(f"Faculties in the {field} field:")
            found_matching_faculties = False
            for faculty in self.faculties:
                if faculty.get_study_field() == field:
                    found_matching_faculties = True
                    print(f"{faculty.get_name()} ({faculty.get_abbreviation()})")
            if not found_matching_faculties:
                print(f"No faculties found for the field: {field_input}")
        except KeyError:
            print(f"Invalid field name: {field_input}")

    def create_and_assign_student(self):
        print(
            "Please enter student details in the format: <faculty abbreviation>/<firstname>/<lastname>/<email>/<enrollmentDate>/<dateOfBirth>")
        student_input = self.scanner()
        student_details = Tools.parse_input(student_input)

        if len(student_details) != 6:
            print(
                "Invalid input format. Please use the format: <faculty abbreviation>/<firstname>/<lastname>/<email>/<enrollmentDate>/<dateOfBirth>")
            return

        faculty_abbreviation, first_name, last_name, email, enrollment_date_input, date_of_birth_input = student_details

        try:
            enrollment_date = Tools.parse_date(enrollment_date_input)
            date_of_birth = Tools.parse_date(date_of_birth_input)
        except ValueError:
            print("Invalid date format. Please use the format: yyyy-MM-dd")
            return

        new_student = Student(first_name, last_name, email, enrollment_date, date_of_birth, False)

        for faculty in self.faculties:
            if faculty.get_abbreviation() == faculty_abbreviation:
                faculty.get_students().append(new_student)
                Logger.log_student_creation(new_student, faculty)
                print(f"Student created and assigned to the faculty: {faculty.get_name()}")
                self.save_university_state()
                return

        print(f"Faculty with abbreviation {faculty_abbreviation} not found.")

    def graduate_student(self):
        print("Please enter student data in the format <first name>/<last name>/<faculty>")
        student_data = self.scanner()
        student_details = Tools.parse_input(student_data)

        if len(student_details) != 3:
            print("Invalid input format. Please use <first name>/<last name>/<faculty>.")
            return

        first_name, last_name, faculty_name = student_details

        faculty = self.find_faculty_by_name(faculty_name)
        if not faculty:
            print(f"Faculty with name {faculty_name} not found.")
            return

        for student in faculty.get_students():
            if student.get_first_name() == first_name and student.get_last_name() == last_name:
                if not student.get_graduated():
                    student.set_graduated(True)
                    Logger.log_student_graduation(student)
                    print(f"Student {first_name} {last_name} in {faculty_name} has been graduated.")
                else:
                    print(f"Student {first_name} {last_name} in {faculty_name} is already graduated.")
                self.save_university_state()
                return

        print(f"Student {first_name} {last_name} not found in {faculty_name}.")

    def display_students(self, check):
        print("Please enter the faculty name of students you want to see:")
        faculty_name = self.scanner()
        found_students = False
        for faculty in self.faculties:
            if faculty.get_name().lower() == faculty_name.lower():
                for student in faculty.get_students():
                    if (not check and not student.get_graduated()) or (check and student.get_graduated()):
                        found_students = True
                        print(f"{student.get_first_name()} {student.get_last_name()}")
        if not found_students:
            if check:
                print("No graduates found.")
            else:
                print("No currently enrolled students found.")

    def check_student_belongs_to_faculty(self):
        print("Please enter the student details in the format <first name>/<last name>/<faculty abbreviation>")
        student_data = self.scanner()
        student_details = Tools.parse_input(student_data)

        if len(student_details) != 3:
            print("Invalid input format. Please use the format: <first name>/<last name>/<faculty abbreviation>")
            return

        first_name, last_name, faculty_abbreviation = student_details

        faculty = self.find_faculty_by_abbreviation(faculty_abbreviation)
        if not faculty:
            print(f"Faculty with abbreviation {faculty_abbreviation} not found.")
        else:
            student_belongs_to_faculty = faculty.contains_student(first_name, last_name)
            if student_belongs_to_faculty:
                print(f"{first_name} {last_name} belongs to {faculty.get_name()}")
            else:
                print(f"{first_name} {last_name} does not belong to {faculty.get_name()}")

    def save_university_state(self):
        FileManager.save_university_state(self.get_all_faculties())
