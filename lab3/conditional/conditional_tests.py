import unittest
import conditional


class TestCases(unittest.TestCase):
    def test_max_101(self):
        self.assertEqual(conditional.max_101(3, 4), 4)
        self.assertEqual(conditional.max_101(1, 5), 5)
        pass

    def test_max_of_three(self):
        self.assertEqual(conditional.max_of_three(1, 2, 3), 3)
        self.assertEqual(conditional.max_of_three(3, 1, 2), 3)
        self.assertEqual(conditional.max_of_three(2, 1, 3), 3)
        self.assertEqual(conditional.max_of_three(1, 3, 2), 3)
        self.assertEqual(conditional.max_of_three(2, 3, 1), 3)
        self.assertEqual(conditional.max_of_three(2, 1, 3), 3)
        self.assertEqual(conditional.max_of_three(3, 2, 1), 3)
        pass

    def test_rental_late_fee(self):
        self.assertEqual(conditional.rental_late_fee(0), 0)
        self.assertEqual(conditional.rental_late_fee(10), 5)
        self.assertEqual(conditional.rental_late_fee(20), 7)
        self.assertEqual(conditional.rental_late_fee(24), 19)
        self.assertEqual(conditional.rental_late_fee(50), 100)
        pass

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
