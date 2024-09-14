import pytest
from src.Types import DataType
from src.CalcDebtStudents import CalcDebtStudents


class TestCalcDebtStudents:
    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Сидоров Иван Иванович": [
                ("химия", 100),
                ("физика", 48)
            ]
        }

    def test_count_debt_students(self, input_data: DataType) -> None:
        debt_calculator = CalcDebtStudents(input_data)
        assert debt_calculator.count_debt_students() == 1

    def test_print_result(self, input_data: DataType, capsys) -> None:
        debt_calculator = CalcDebtStudents(input_data)
        debt_calculator.print_result()
        captured = capsys.readouterr()
        assert "Количество студентов с задолженностями: 1" in captured.out
