from enums.SudyField import StudyField

class Faculty:
    def __init__(self, name, abbreviation, students, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.study_field = study_field

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_abbreviation(self):
        return self.abbreviation

    def get_study_field(self):
        return self.study_field

    def get_students(self):
        return self.students

    def contains_student(self, first_name, last_name):
        for student in self.students:
            if student.get_first_name() == first_name and student.get_last_name() == last_name:
                return True
        return False

    def __str__(self):
        return f"Faculty(name='{self.name}', abbreviation='{self.abbreviation}', students={self.students}, study_field={self.study_field})"
