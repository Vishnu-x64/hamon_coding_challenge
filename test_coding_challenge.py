import unittest
from coding_challenge import f


class TestInitialFunction(unittest.TestCase):

    def test_string_input(self):
        data = "malayalam"
        self.assertEqual(f(data), {"m": 2, "a": 4, "l": 2, "y": 1})

    def test_list_input(self):
        data = ["m", "a", "l", "a", "y", "a", "l", "a", "m"]
        self.assertEqual(f(data), {"m": 2, "a": 4, "l": 2, "y": 1})

    def test_tuple_input(self):
        data = (1, 2, 2, 3, 1)
        self.assertEqual(f(data), {1: 2, 2: 2, 3: 1})

    def test_empty_iterable(self):
        self.assertEqual(f(""), {})  # empty string
        self.assertEqual(f([]), {})  # empty list
        self.assertEqual(f(()), {})  # emtpy tuple

    def test_non_iterable_fails(self):
        with self.assertRaises(TypeError):
            f(1)


if __name__ == "__main__":
    unittest.main()
