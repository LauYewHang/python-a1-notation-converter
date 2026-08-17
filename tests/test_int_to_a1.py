import unittest
from ..src.a1_notation_converter import a1_converter

class TestIntToA1(unittest.TestCase):
    def test_single_digit(self):
        print("")
        for i in range(1, a1_converter.ALPHABET_AMOUNT + 1):
            a1_notation = a1_converter.int_to_a1(i)
            print(f"i: {i}\t\ta1_notation: {a1_notation}")
            self.assertEqual(a1_notation, chr(i - 1 + a1_converter.ASCII_A_INDEX))

    def test_double_digit(self):
        print("")
        for i in range(27, a1_converter.ALPHABET_AMOUNT * a1_converter.ALPHABET_AMOUNT + a1_converter.ALPHABET_AMOUNT + 1):
            a1_notation = a1_converter.int_to_a1(i)
            print(f"i: {i}\t\ta1_notation: {a1_notation}")
            self.assertEqual(
                a1_notation, 
                f"{chr(((i - a1_converter.ALPHABET_AMOUNT if i%a1_converter.ALPHABET_AMOUNT == 0 else i - i%a1_converter.ALPHABET_AMOUNT) // a1_converter.ALPHABET_AMOUNT) - 1 + a1_converter.ASCII_A_INDEX)}"
                f"{chr((i%a1_converter.ALPHABET_AMOUNT if i%a1_converter.ALPHABET_AMOUNT > 0 else a1_converter.ALPHABET_AMOUNT) - 1 + a1_converter.ASCII_A_INDEX)}"
            )

    def test_tripple_digit(self):
        print("")
        print(f"i: 703\t\ta1_notation: {a1_converter.int_to_a1(703)}")
        self.assertEqual(a1_converter.int_to_a1(703), "AAA")
        print(f"i: 18278\ta1_notation: {a1_converter.int_to_a1(18278)}")
        self.assertEqual(a1_converter.int_to_a1(18278), "ZZZ")

    def test_quadruple_digit(self):
        print("")
        print(f"i: 18279\ta1_notation: {a1_converter.int_to_a1(18279)}")
        self.assertEqual(a1_converter.int_to_a1(18279), "AAAA")
        print(f"i: 475254\ta1_notation: {a1_converter.int_to_a1(475254)}")
        self.assertEqual(a1_converter.int_to_a1(475254), "ZZZZ")

if __name__ == "__main__":
    unittest.main()
