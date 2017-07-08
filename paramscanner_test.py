import unittest

from argparser import ParamScanner


class TestParamScanner(unittest.TestCase):
    def test_splits_command_line_arguments_in_groups(self):
        self.assertEqual(ParamScanner().get_groups("-l -p 8080 -b /usr/local/log"), [
            ("-l", True),
            ("-p", '8080'),
            ("-b", "/usr/local/log")])


if __name__ == "__main__":
    unittest.main()
