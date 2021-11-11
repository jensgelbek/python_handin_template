from typing import List

from modules_w3.course import Course


class Data_Sheet():
    def __init__(self, courses: List[Course]):
        self.courses = courses

    def get_grades_as_list(self):
        result = []
        for course in self.courses:
            if course.grade != "none":
                result.append(course.grade)
        return result
