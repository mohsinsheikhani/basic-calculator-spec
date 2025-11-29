# Basic Calculator Module Specification

## User Stories

### Addition
**As a developer**, I want to add two numbers, so that I can perform basic arithmetic calculations in my application.

### Subtraction
**As a developer**, I want to subtract one number from another, so that I can calculate differences and decrements in my code.

### Multiplication
**As a developer**, I want to multiply two numbers, so that I can compute products and scaling operations.

### Division
**As a developer**, I want to divide one number by another, so that I can calculate ratios and proportional values.

### Error Handling
**As a developer**, I want the calculator to handle invalid inputs gracefully, so that my application doesn't crash when users provide bad data.

## API Specification

```python
def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers."""

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a."""

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers."""

def divide(a: int | float, b: int | float) -> float:
    """Divide a by b. Always returns float."""
```

## Acceptance Criteria

### Addition: `add(a, b)`
- **Happy Path:** `add(5, 3)` → `8`
- **Zero Identity:** `add(x, 0)` → `x`
- **Negatives:** `add(-3, -7)` → `-10`
- **Mixed Types:** `add(5, 3.5)` → `8.5`
- **Type Error:** `add("5", 3)` → `TypeError`

### Subtraction: `subtract(a, b)`
- **Happy Path:** `subtract(10, 3)` → `7`
- **Zero Identity:** `subtract(5, 0)` → `5`
- **Negative Result:** `subtract(3, 10)` → `-7`
- **Mixed Types:** `subtract(10.5, 3)` → `7.5`
- **Type Error:** `subtract(10, "3")` → `TypeError`

### Multiplication: `multiply(a, b)`
- **Happy Path:** `multiply(4, 5)` → `20`
- **Zero Absorbing:** `multiply(5, 0)` → `0`
- **Negatives:** `multiply(-3, 4)` → `-12`
- **Mixed Types:** `multiply(2.5, 4)` → `10.0`
- **Type Error:** `multiply(None, 5)` → `TypeError`

### Division: `divide(a, b)`
- **Happy Path:** `divide(10, 2)` → `5.0`
- **Zero Dividend:** `divide(0, 5)` → `0.0`
- **Negatives:** `divide(-10, 2)` → `-5.0`
- **Mixed Types:** `divide(7, 2.0)` → `3.5`
- **Division by Zero:** `divide(10, 0)` → `ZeroDivisionError("Cannot divide by zero")`
- **Type Error:** `divide(10, "2")` → `TypeError`

## Design Decisions

### 1. Floating Point Precision
- **Behavior:** Accept Python's native floating point behavior
- **Example:** `add(0.1, 0.2)` → `0.30000000000000004`
- **Rationale:** Keep implementation simple; users needing precision use `decimal.Decimal`

### 2. Division by Zero
- **Behavior:** Raise `ZeroDivisionError("Cannot divide by zero")`
- **Rationale:** Explicit error handling over silent special values

### 3. Type Preservation
- **Rules:** Return `int` only when both inputs are `int` AND result has no fractional part
- **Division Exception:** Always returns `float`
- **Examples:**
  - `add(5, 3)` → `8` (int)
  - `add(5, 3.0)` → `8.0` (float)
  - `divide(10, 2)` → `5.0` (always float)

### 4. Zero Behavior
- **Addition/Subtraction:** Identity element (`x + 0 = x`, `x - 0 = x`)
- **Multiplication:** Absorbing element (`x * 0 = 0`)
- **Division:** `0 / x = 0.0` (when x ≠ 0)

### 5. Negative Numbers
- **Behavior:** Standard arithmetic rules apply
- **No special handling required**

### 6. Large Numbers
- **Integers:** Python's arbitrary precision (no artificial limits)
- **Floats:** IEEE 754 limits (`~1.8e308`)
- **Overflow:** Natural `OverflowError` when exceeded

## Input Validation

### Accepted Types
- `int`: Any Python integer
- `float`: Any Python float

### Rejected Types
- Strings, None, lists, objects → `TypeError`
- Complex numbers → `TypeError`

## Error Messages

- **Type Error:** Default Python `TypeError` message
- **Division by Zero:** `ZeroDivisionError("Cannot divide by zero")`

## Out of Scope

- Decimal precision handling
- Complex number support
- Vector/matrix operations
- Trigonometric functions
- Input parsing from strings
- Result formatting/rounding
- Performance optimization for large datasets
