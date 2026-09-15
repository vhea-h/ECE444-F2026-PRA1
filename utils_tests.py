import utils
import unittest

print(utils.utils.formatter(5))

class TestReversed(unittest.TestCase):
    def test_reverse_int(self):
        self.assertEqual(utils.utils.reversed(123), 321)

    def test_reverse_float(self):
        with self.assertRaises(TypeError):
            utils.utils.reversed(3.1415)

    def test_reverse_string(self):
            with self.assertRaises(TypeError):
                utils.utils.reversed("haha")

class TestFormatted(unittest.TestCase):
    def test_small_formatter_int(self):
        self.assertEqual(utils.utils.formatter(5), ('0b101', '0o5'))

    def test_large_formatter_int(self):
            self.assertEqual(utils.utils.formatter(35), ('0b100011', '0o43'))

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.utils.formatter(3.1415)

    def test_formatter_string(self):
            with self.assertRaises(TypeError):
                utils.utils.formatter("haha")


if __name__ == '__main__':
    unittest.main()