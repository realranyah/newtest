# calculator.py

def add(a, b):
    """Add two numbers."""
    return float(a + b)

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b, returns None if dividing by zero."""
    if b == 0:
        return None
    return a / b
