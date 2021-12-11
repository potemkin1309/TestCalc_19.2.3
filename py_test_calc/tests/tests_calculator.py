import pytest
from app.mycalculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 16, 4) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 5) == 13

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 17, 10) == 7