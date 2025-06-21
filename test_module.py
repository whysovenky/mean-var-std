import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate_correct(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555555, 0.6666666666666666, 10.666666666666666], [4.0, 10.666666666666666, 7.555555555555555], 6.987654320987654],
            'standard deviation': [[3.091206165165235, 0.816496580927726, 3.265986323710904], [2.0, 3.265986323710904, 2.7495454169735034], 2.643417167415949],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        for key in expected:
            self.assertAlmostEqual(actual[key][2], expected[key][2], places=1)

    def test_calculate_raises_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3, 4])  # not 9 elements
