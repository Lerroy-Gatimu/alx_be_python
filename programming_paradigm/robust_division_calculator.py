# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero and invalid input errors.
    """

    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
