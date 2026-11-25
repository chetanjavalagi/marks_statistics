import unittest
from marks_statistics import (
    validate_marks,
    total_marks,
    average_marks,
    highest_marks,
    lowest_marks,
)


class TestMarksStatistics(unittest.TestCase):
    def test_validate_marks_valid(self):
        marks = [80, 90.5, 0, 100]
        self.assertEqual(validate_marks(marks), marks)

    def test_validate_marks_empty_raises(self):
        with self.assertRaises(ValueError) as ctx:
            validate_marks([])
        self.assertEqual(str(ctx.exception), "Marks list cannot be empty")

    def test_validate_marks_below_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            validate_marks([75, -1, 85])
        self.assertEqual(str(ctx.exception), "Marks must be between 0 and 100")

    def test_validate_marks_above_hundred_raises(self):
        with self.assertRaises(ValueError) as ctx:
            validate_marks([75, 101, 85])
        self.assertEqual(str(ctx.exception), "Marks must be between 0 and 100")

    def test_total_marks(self):
        self.assertEqual(total_marks([70, 80, 90]), 240)
        self.assertAlmostEqual(total_marks([72.5, 87.5]), 160.0)

    def test_average_marks(self):
        self.assertAlmostEqual(average_marks([70, 80, 90]), 80.0)
        self.assertAlmostEqual(average_marks([50, 75]), 62.5)

    def test_highest_marks(self):
        self.assertEqual(highest_marks([45, 92, 68, 92]), 92)
        self.assertEqual(highest_marks([100]), 100)

    def test_lowest_marks(self):
        self.assertEqual(lowest_marks([45, 92, 0, 68]), 0)
        self.assertAlmostEqual(lowest_marks([55.5, 60.0, 72.2]), 55.5)


if __name__ == "__main__":
    unittest.main()
