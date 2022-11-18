import unittest
from unittest.mock import patch

from lesson14 import my_sum, sum_rows


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class TestMySum(unittest.TestCase):
    def setUpClass() -> None:
        print("\tsetUpClass  TestMySum")

    def tearDownClass():
        print("\ttearDownClass TestMySum")

    def setUp(self):
        print("\t\tsetUp")

    def tearDown(self) -> None:
        print("\t\ttearDown")

    def test_my_sum_fail(self):
        test_data = [1, 2.5, 3]
        actual = my_sum(test_data)
        self.assertEqual("error", actual)

    def test_my_sum_success(self):
        test_data = [1, 2.5, 3]
        actual = my_sum(*test_data)
        self.assertEqual(6.5, actual)

    # def test_my_sum_empty_args(self):
    #     actual = my_sum()
    #     self.assertIsNone(actual)

    def test_my_sum_empty_list(self):
        actual = my_sum([])
        self.assertEqual("error", actual)


class TestSumRows(unittest.TestCase):
    def setUpClass() -> None:
        print("\tsetUpClass  TestLesson14Copy")

    def tearDownClass():
        print("\ttearDownClass TestLesson14Copy")

    def setUp(self):
        print("\t\tsetUp")

    def tearDown(self) -> None:
        print("\t\ttearDown")

    def test_sum_rows_bead(self):
        test_data = [[1, 2.5, 3],
                     [2, 5, 8],
                     [9, 8, 8]]
        actual = sum_rows(test_data)
        self.assertListEqual([6.5, 73, 137], actual)

    @patch("lesson14.my_sum")
    def test_sum_rows(self, mock_sum_row):
        test_data = [[1, 2.5, 3],
                     [2, 5, 8],
                     [9, 8, 8]]
        mock_sum_row.return_value = 1
        actual = sum_rows(test_data)
        self.assertListEqual([1, 1, 1], actual)


if __name__ == "__main__":
    unittest.main()
# coverage run test.py
# coverage html