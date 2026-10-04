import unittest  # Use Python's built-in test runner and assertions.
# from streamlit.testing.v1 import AppTest  # Simulate the Streamlit interface (later lesson).
from calculator import divide, multiply, power ,add  # Import the real backend functions.


class CalculatorTests(unittest.TestCase):  # Group backend behavior checks.
    def test_multiply(self):  # Check one ordinary multiplication.
        self.assertEqual(multiply(6, 4), 24)  # Six times four should be twenty-four.

    def test_divide(self):  # Check one ordinary division.
        self.assertEqual(divide(12, 3), 4)  # Check an exact quotient.



    def test_power(self):
        self.assertEqual(power(2, 3), 8)  # Positive exponent.
        self.assertEqual(power(-2, 3), -8)  # Negative base with an odd exponent.

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Positive exponent.

if __name__ == "__main__":  # Run tests only when this file is executed directly.
    unittest.main()  # Collect tests, print results, and exit with a failure code if needed.
