import os
from models.Faculty import Faculty
from models.Student import Student
from tools.Tools import Tools
from util.Logger import Logger


class BatchOperations:
    ENROLLMENT_FILE_PATH = "C:/Users/user/Desktop/POO/lab_2/databases/enrollment_file.txt"
    GRADUATION_FILE_PATH = "C:/Users/user/Desktop/POO/lab_2/databases/graduation_file.txt"

    def __init__(self, university):
        self.university = university

    def perform_batch_enrollment(self):
        try:
            with open(self.ENROLLMENT_FILE_PATH, 'r') as file:
                for line in file:
                    student_details = Tools.parse_input(line.strip())
                    if len(student_details) == 6:
                        faculty_abbreviation = student_details[0]
                        first_name = student_details[1]
                        last_name = student_details[2]
                        email = student_details[3]
                        enrollment_date_input = student_details[4]
                        date_of_birth_input = student_details[5]

                        try:
                            enrollment_date = Tools.parse_date(enrollment_date_input)
                            date_of_birth = Tools.parse_date(date_of_birth_input)
                        except ValueError as e:
                            print(f"Error parsing dates: {e}")
                            continue

                        new_student = Student(first_name, last_name, email, enrollment_date, date_of_birth, False)
                        faculty = self.university.find_faculty_by_abbreviation(faculty_abbreviation)

                        if faculty:
                            faculty.get_students().append(new_student)
                            Logger.log_student_creation(new_student, faculty)
                        else:
                            print(f"Faculty with abbreviation {faculty_abbreviation} not found.")

            self.university.save_university_state()
            print("Batch enrollment completed successfully.")
        except IOError as e:
            print(f"Error during batch enrollment: {e}")

    def perform_batch_graduation(self):
        try:
            with open(self.GRADUATION_FILE_PATH, 'r') as file:
                for line in file:
                    student_details = line.strip().split('/')
                    if len(student_details) == 3:
                        first_name = student_details[0]
                        last_name = student_details[1]
                        faculty_name = student_details[2]

                        faculty = self.university.find_faculty_by_name(faculty_name)
                        if faculty:
                            for student in faculty.get_students():
                                if student.get_first_name() == first_name and student.get_last_name() == last_name:
                                    if not student.get_graduated():
                                        student.set_graduated(True)
                                        Logger.log_student_graduation(student)
                                    break
                        else:
                            print(f"Faculty with name {faculty_name} not found.")

            self.university.save_university_state()
            print("Batch graduation completed successfully.")
        except IOError as e:
            print(f"Error during batch graduation: {e}")
