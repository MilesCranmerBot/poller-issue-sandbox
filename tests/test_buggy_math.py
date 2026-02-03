import unittest

import buggy_math


class TestMean(unittest.TestCase):
    def test_mean_basic(self):
        self.assertAlmostEqual(buggy_math.mean([1, 2, 3]), 2.0)

    def test_mean_singleton(self):
        self.assertAlmostEqual(buggy_math.mean([5]), 5.0)

    def test_mean_empty_raises(self):
        with self.assertRaises(ValueError):
            buggy_math.mean([])


if __name__ == "__main__":
    unittest.main()
