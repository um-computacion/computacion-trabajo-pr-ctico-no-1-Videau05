import unittest
from src.roman_converter import decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(5), "V")
        self.assertEqual(decimal_to_roman(10), "X")
        self.assertEqual(decimal_to_roman(50), "L")
        self.assertEqual(decimal_to_roman(100), "C")
        self.assertEqual(decimal_to_roman(500), "D")
        self.assertEqual(decimal_to_roman(1000), "M")

    def test_addition_rules(self):
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(6), "VI")
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(101), "CI")

    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman(40), "XL")
        self.assertEqual(decimal_to_roman(90), "XC")
        self.assertEqual(decimal_to_roman(400), "CD")
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(1987), "MCMLXXXVII")
        self.assertEqual(decimal_to_roman(2023), "MMXXIII")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)
        with self.assertRaises(ValueError):
            decimal_to_roman(-10)

if __name__ == '__main__':
    unittest.main()