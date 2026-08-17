import unittest
from ..src.a1_notation_converter import a1_converter

class TestA1ToInt(unittest.TestCase):
    def test_single_alphabet(self):
        print("")
        for i in range(1, a1_converter.ALPHABET_AMOUNT + 1):
            print(f"a1_notation: {a1_converter.int_to_a1(i)}\t\ti: {i}")
            self.assertEqual(i, a1_converter.a1_to_int(chr(i - 1 + a1_converter.ASCII_A_INDEX)))

    def test_double_alphabet(self):
        print("")
        for i in range(27, a1_converter.ALPHABET_AMOUNT * a1_converter.ALPHABET_AMOUNT + a1_converter.ALPHABET_AMOUNT + 1):
            a1_notation = a1_converter.int_to_a1(i)
            print(f"a1_notation: {a1_notation}\t\ti: {i}")
            self.assertEqual(i, a1_converter.a1_to_int(a1_notation))

    def test_tripple_alphabet(self):
        print("")
        print(f"a1_notation: AAA\t\ti: {a1_converter.a1_to_int('AAA')}")
        self.assertEqual(703, a1_converter.a1_to_int("AAA"))
        print(f"a1_notation: ZZZ\t\ti: {a1_converter.a1_to_int('ZZZ')}")
        self.assertEqual(18278, a1_converter.a1_to_int("ZZZ"))

    def test_quadruple_digit(self):
        print("")
        print(f"a1_notation: AAAA\t\ti: {a1_converter.a1_to_int('AAAA')}")
        self.assertEqual(18279, a1_converter.a1_to_int("AAAA"))
        print(f"a1_notation: ZZZZ\t\ti: {a1_converter.a1_to_int('ZZZZ')}")
        self.assertEqual(475254, a1_converter.a1_to_int("ZZZZ"))

if __name__ == "__main__":
    unittest.main()
