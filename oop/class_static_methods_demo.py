# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers without accessing class data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Accesses class attribute and multiplies two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
