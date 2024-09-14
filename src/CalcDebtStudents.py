import json
from Types import DataType
from DataReader import DataReader


class CalcDebtStudents:
    def __init__(self, data: DataType):
        self.data = data

    def count_debt_students(self) -> int:
        debt_students = 0
        for students, subjects in self.data.items():
            for subject, score in subjects:
                if score < 61:
                    debt_students += 1
                    break

        return debt_students

    def print_result(self):
        debt_count = self.count_debt_students()
        print(f"Количество студентов с задолженностями: {debt_count}")
