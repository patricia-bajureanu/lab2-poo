from datetime import datetime

class Tools:
    @staticmethod
    def parse_input(input_str):
        return input_str.split("/")

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d')

    @staticmethod
    def format_date(date):
        return date.strftime('%Y-%m-%d')
