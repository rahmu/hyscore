import operator
import types
import unittest

import hy
from context import hyscore


def double(x):
    return x*x


class HyscoreTest(unittest.TestCase):

    def test_map(self):
        result = hyscore.map(double, range(4))
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [0, 1, 4, 9])

    def test_filter(self):
        result = hyscore.filter(lambda x: x > 5, range(10))
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [6, 7, 8, 9])

    def test_find(self):
        result = hyscore.find(lambda x: x > 5, range(10))
        self.assertEqual(result, 6)

        result = hyscore.find(lambda x: x > 10, range(10))
        self.assertIsNone(result)

    def test_fold_left(self):
        result = hyscore.fold_left(operator.sub,
                                   range(6),
                                   1000)
        self.assertEqual(result, 985)

        result = hyscore.fold_left(operator.sub, [], 1000)
        self.assertEqual(result, 1000)

    def test_fold_right(self):
        result = hyscore.fold_right(operator.sub,
                                    range(6),
                                    1000)
        self.assertEqual(result, 997)

        result = hyscore.fold_right(operator.sub, [], 1000)
        self.assertEqual(result, 1000)


if __name__ == "__main__":
    unittest.main()
