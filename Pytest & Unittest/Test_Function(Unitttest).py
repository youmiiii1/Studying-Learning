import unittest
from Function import is_even_number

class IsEvenNumber(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_even_number(2))
        self.assertTrue(is_even_number(4))

    def test_invalid(self):
        self.assertFalse(is_even_number(1))
        self.assertFalse(is_even_number(3))

    def test_edge_cases(self):
        self.assertEqual(is_even_number(1), False)
        self.assertEqual(is_even_number(-1), False)
        self.assertEqual(is_even_number(0), True)
        self.assertEqual(is_even_number(2), True)
        self.assertEqual(is_even_number(-2), True)

    def test_error(self):
        with self.assertRaises(ValueError):
            is_even_number("1")

        with self.assertRaises(ValueError):
            is_even_number(True)

        with self.assertRaises(ValueError):
            is_even_number(())

        with self.assertRaises(ValueError):
            is_even_number([])

        with self.assertRaises(ValueError):
            is_even_number({})

        with self.assertRaises(ValueError):
            is_even_number(1.5)