from ..sqlent.helpers import proper_where_value
import unittest

class TestProperWhereValue(unittest.TestCase):
    def test_int(self):
        self.assertEqual(1 , proper_where_value(1))

    def test_float(self):
        self.assertEqual(1.0 , proper_where_value(1.0))

    def test_string(self):
        self.assertEqual("'water'", proper_where_value('water'))

    def test_array_of_int(self):
        self.assertEqual("(1, 2, 3)", proper_where_value([1,2,3]))

    def test_array_of_string(self):
        self.assertEqual("('1', '2', '3')", proper_where_value(['1','2','3']))
