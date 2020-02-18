import unittest
import random
from count_sort import *


class IterativeSortingTest(unittest.TestCase):

    # Uncomment this test to test your count_sort implementation
    def test_counting_sort(self):

        arr4 = random.sample(range(20000), 2000)

        self.assertEqual(count_sort(arr4, 20000), sorted(arr4))


if __name__ == '__main__':
    unittest.main()
