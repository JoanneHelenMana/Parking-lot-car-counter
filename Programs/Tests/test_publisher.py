import unittest
from Programs.Count_cars.publisher import Publisher


class TestPublisher(unittest.TestCase):
    def setUp(self):
        self.uut = Publisher()

    def test_update_is_type_dict(self):
        self.assertIs(Publisher.get_update(), dict)


if __name__ == '__main__':
    unittest.main()
