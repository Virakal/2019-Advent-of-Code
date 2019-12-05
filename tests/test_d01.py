from advent.d01 import calculate_fuel_cost

import unittest


class Day01Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calculate_fuel_cost(12), 2)

    def test_2(self):
        self.assertEqual(calculate_fuel_cost(14), 2)

    def test_3(self):
        self.assertEqual(calculate_fuel_cost(1969), 654)

    def test_4(self):
        self.assertEqual(calculate_fuel_cost(100756), 33583)


if __name__ == "__main__":
    unittest.main()
