from modules_w3.data_sheet import Data_Sheet


class Student():
    def __init__(self, name, gender, data_sheet: Data_Sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return sum(grades)/len(grades)
