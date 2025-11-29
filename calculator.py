"""Basic calculator module with four arithmetic operations."""


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers.
    
    Examples:
        >>> add(5, 3)
        8
        >>> add(5, 3.5)
        8.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a.
    
    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(3, 10)
        -7
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers.
    
    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 4)
        10.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide a by b. Always returns float.
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError()
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
