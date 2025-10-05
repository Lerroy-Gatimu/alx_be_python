import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for addition ---
    def test_addition_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(5, -3), 2)

    def test_addition_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # --- Tests for subtraction ---
    def test_subtraction_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_signs(self):
        """Test subtraction involving positive and negative numbers."""
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_with_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Tests for multiplication ---
    def test_multiplication_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiplication_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_signs(self):
        """Test multiplication involving positive and negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_multiplication_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Tests for division ---
    def test_division_positive_numbers(self):
        """Test division of two positive numbers."""
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_division_negative_numbers(self):
        """Test division of two negative numbers."""
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_division_mixed_signs(self):
        """Test division involving positive and negative numbers."""
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_division_with_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        """Test division when denominator is zero (should return None)."""
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_floats(self):
        """Test division with floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

# Run all tests
if __name__ == "__main__":
    unittest.main()
