import unittest

from main import factors_of


class TestPrimeFactors(unittest.TestCase):
    def test_start(self):
        assert 1 == 1

    def test_factors_of_1(self):
        assert not factors_of(1)

    def test_factors_of_2(self):
        assert factors_of(2) == [2]

    def test_factors_of_3(self):
        assert factors_of(3) == [3]

    def test_factors_of_4(self):
        assert factors_of(4) == [2, 2]

    def test_factors_of_5(self):
        assert factors_of(5) == [5]

    def test_factors_of_6(self):
        assert factors_of(6) == [2, 3]

    def test_factors_of_7(self):
        assert factors_of(7) == [7]

    def test_factors_of_8(self):
        assert factors_of(8) == [2, 2, 2]
