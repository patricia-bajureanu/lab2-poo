import sys


class AppLoop:
    def __init__(self):
        from models.University import University
        from util.BatchOperations import BatchOperations
        self.scanner = input
        self.university = University()
        self.batch_operations = BatchOperations(self.university)

    def run(self):
        print("WELCOME TO THE STUDENT MANAGEMENT SYSTEM !")
        while True:
            self.display_main_menu()
            choice = self.get_user_choice()

            if choice == 'g':
                self.general_operations_menu()
            elif choice == 'f':
                self.faculty_operations_menu()
            elif choice == 's':
                self.student_menu()
            elif choice == 'q':
                self.quit_program()
            else:
                print("Invalid choice. Please select a valid option.")

    def display_main_menu(self):
        print("""
                What do you want to do?
                g - General operations
                f - Faculty operations
                s - Student operations

                q - Quit program
        """)

    def display_general_menu(self):
        print("""
                -------------------------------------------------------------------
                You are currently in the General menu. What do you want to do next?
                nf - Create a new faculty
                ssf - Search what faculty a student belongs to
                uf - Display university faculties
                df - Display all faculties belonging to a specific field

                b - Back to main menu
                q - Quit program
        """)

    def display_faculty_menu(self):
        print("""
                You are currently in the Faculty menu. What do you want to do next?
                cs - Create and assign student to a faculty
                gs - Graduate student from a faculty
                des - Display current enrolled students
                dg - Display graduates
                bf - Tell if a student belongs to a faculty

                b - Back to main menu
                q - Quit program
        """)

    def display_student_menu(self):
        print("""
                You are currently in the Student menu. What do you want to do next?
                 be - Perform students' batch enrollment via enrollment_file.txt
                 bg - Perform students batch graduation via graduation_file.txt

                 b - Back to main menu
                 q - Quit program
        """)

    def get_user_choice(self):
        return input("Enter your choice: ").strip().lower()

    def general_operations_menu(self):
        while True:
            self.display_general_menu()
            choice = self.get_user_choice()

            if choice == 'nf':
                self.university.create_faculty()
            elif choice == 'ssf':
                self.university.search_student_faculty()
            elif choice == 'uf':
                self.university.display_university_faculties()
            elif choice == 'df':
                self.university.display_faculties_by_field()
            elif choice == 'b':
                return
            elif choice == 'q':
                self.quit_program()
            else:
                print("Invalid choice. Please select a valid option.")

    def faculty_operations_menu(self):
        while True:
            self.display_faculty_menu()
            choice = self.get_user_choice()

            if choice == 'cs':
                self.university.create_and_assign_student()
            elif choice == 'gs':
                self.university.graduate_student()
            elif choice == 'des':
                self.university.display_students(False)
            elif choice == 'dg':
                self.university.display_students(True)
            elif choice == 'bf':
                self.university.check_student_belongs_to_faculty()
            elif choice == 'b':
                return
            elif choice == 'q':
                self.quit_program()
            else:
                print("Invalid choice. Please select a valid option.")

    def student_menu(self):
        while True:
            self.display_student_menu()
            choice = self.get_user_choice()

            if choice == 'be':
                self.batch_operations.perform_batch_enrollment()
            elif choice == 'bg':
                self.batch_operations.perform_batch_graduation()
            elif choice == 'b':
                return
            elif choice == 'q':
                self.quit_program()
            else:
                print("Invalid choice. Please select a valid option.")

    def quit_program(self):
        print("Exiting the program. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    app = AppLoop()
    app.run()
