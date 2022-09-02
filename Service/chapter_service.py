import csv
import os


class ChapterService:
    @staticmethod
    def read_predict_from_csv():
        if os.path.exists("../Data/chapters.csv"):
            reader = open("../Data/chapters.csv", "r", encoding='UTF8')
            return csv.DictReader(reader)
        return {}
