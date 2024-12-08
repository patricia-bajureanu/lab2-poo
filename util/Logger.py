from datetime import datetime

class Logger:
    LOG_FILE_PATH = "C:/Users/user/Desktop/POO/lab_2/databases/log.txt"

    @staticmethod
    def log_student_creation(student, faculty):
        Logger.log(f"Student created: {student.get_first_name()} {student.get_last_name()} "
                   f"and assigned to {faculty.get_name()}")

    @staticmethod
    def log_student_graduation(student):
        Logger.log(f"Student graduated: {student.get_first_name()} {student.get_last_name()}")

    @staticmethod
    def log_faculty_creation(faculty):
        Logger.log(f"Faculty created: {faculty.get_name()}")

    @staticmethod
    def log(message):
        try:
            with open(Logger.LOG_FILE_PATH, 'a', encoding='utf-8') as log_file:
                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{formatted_time} - {message}\n")
        except IOError as e:
            print(f"Error writing to log file: {e}")
