import unittest
from unittest.mock import patch

from argparser import ArgParser


class TestAcceptance(unittest.TestCase):
    def test_updates_parameter_values_from_command_line_arguments(self):
        with patch('argparser.ParamScanner') as mock:
            mock.return_value.get_groups.return_value = [
                ("-l", True),
                ("-p", 8080),
                ("-b", "/usr/local/log")
            ]
            parser = ArgParser(schema={"-l", ("-p", 8000), ("-b", "/usr/log")})
            parser.parse("-l -p 8080 -b /usr/local/log")
            self.assertEqual(parser.get("-l"), True)
            self.assertEqual(parser.get("-p"), 8080)
            self.assertEqual(parser.get("-b"), "/usr/local/log")


if __name__ == "__main__":
    unittest.main()
