import unittest
from Programs.Configuration.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    def setUp(self):
        self.uut = Configuration()

    def test_read_configuration_file(self):
        self.assertEqual(Configuration.from_file()['location'], 'Joondalup City Square Parking')
        self.assertEqual(Configuration.from_file()['number-of-spaces'], '192')
        self.assertEqual(Configuration.from_file()['available-spaces'], '4')
        self.assertEqual(Configuration.from_file()['broker-host'], 'localhost')
        self.assertEqual(Configuration.from_file()['broker-port'], '1883')

    def test_ignore_empty_line(self):
        self.assertNotIn('', Configuration.from_file())


if __name__ == '__main__':
    unittest.main()
