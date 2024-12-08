from datetime import date

class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth, graduated):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.graduated = graduated

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_graduated(self):
        return self.graduated

    def set_graduated(self, graduated):
        self.graduated = graduated

    def get_enrollment_date(self):
        return self.enrollment_date

    def get_date_of_birth(self):
        return self.date_of_birth
