from enums.SudyField import StudyField
from models.Faculty import Faculty
from models.Student import Student
from tools.Tools import Tools



class FileManager:
    SAVE_FILE_PATH = "C:/Users/user/Desktop/POO/lab_2/databases/university.txt"

    @staticmethod
    def save_university_state(faculties):
        try:
            with open(FileManager.SAVE_FILE_PATH, 'w', encoding='utf-8') as file:
                for faculty in faculties:
                    file.write(
                        f"Faculty: {faculty.get_name()},{faculty.get_abbreviation()},{faculty.get_study_field().name}\n")
                    for student in faculty.get_students():
                        file.write(
                            f"Student: {student.get_first_name()},{student.get_last_name()},{student.get_email()},"
                            f"{Tools.format_date(student.get_enrollment_date())},"
                            f"{Tools.format_date(student.get_date_of_birth())},"
                            f"{student.get_graduated()}\n")
        except IOError as e:
            print(f"Error while saving university state: {e}")

    @staticmethod
    def load_university_state():
        faculties = []
        current_faculty = None
        try:
            with open(FileManager.SAVE_FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("Faculty:"):
                        parts = line.split(",")
                        if len(parts) >= 3:
                            faculty_name = parts[0].replace("Faculty:", "").strip()
                            faculty_abbreviation = parts[1].strip()
                            study_field = StudyField[parts[2].strip()]
                            current_faculty = Faculty(faculty_name, faculty_abbreviation, [], study_field)
                            faculties.append(current_faculty)
                    elif line.startswith("Student:") and current_faculty:
                        parts = line.split(",")
                        if len(parts) >= 6:
                            first_name = parts[0].replace("Student:", "").strip()
                            last_name = parts[1].strip()
                            email = parts[2].strip()
                            enrollment_date = Tools.parse_date(parts[3].strip())
                            date_of_birth = Tools.parse_date(parts[4].strip())
                            graduated = parts[5].strip().lower() == 'true'
                            student = Student(first_name, last_name, email, enrollment_date, date_of_birth, graduated)
                            current_faculty.get_students().append(student)
            print("University state loaded successfully.")
        except (IOError, ValueError) as e:
            print(f"Error while loading university state: {e}")
        return faculties

