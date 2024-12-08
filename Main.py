from behavior.AppLoop import AppLoop
from models.University import University
from util.FileManager import FileManager


def main():
    saved_faculties = FileManager.load_university_state()

    university = University()

    if saved_faculties:
        university.get_all_faculties().extend(saved_faculties)

    app_loop = AppLoop()
    app_loop.run()


if __name__ == "__main__":
    main()
