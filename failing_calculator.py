def average_ratios(numbers):
    """
    Calculate average of ratios (100 / each number).

    Args:
        numbers: List of numbers (must not contain zero)

    Returns:
        Average of the ratios

    Raises:
        ValueError: If list is empty or contains zero
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    if any(n == 0 for n in numbers):
        raise ValueError("List cannot contain zero (division by zero)")

    total = sum(100 / num for num in numbers)
    return total / len(numbers)


# Test cases
if __name__ == "__main__":
    # Test 1: Valid input
    try:
        result = average_ratios([10, 5])
        assert abs(result - 15.0) < 0.01, f"Expected ~15.0, got {result}"
        print(f"[PASS] Test 1: average_ratios([10, 5]) = {result}")
    except Exception as e:
        print(f"[FAIL] Test 1: {e}")

    # Test 2: Division by zero - should raise error gracefully
    try:
        result = average_ratios([10, 5, 0])
        print(f"[FAIL] Test 2: Should have raised ValueError")
    except ValueError as e:
        print(f"[PASS] Test 2: Caught error gracefully - {e}")

    # Test 3: Another valid case
    try:
        result = average_ratios([20])
        assert abs(result - 5.0) < 0.01, f"Expected 5.0, got {result}"
        print(f"[PASS] Test 3: average_ratios([20]) = {result}")
    except Exception as e:
        print(f"[FAIL] Test 3: {e}")

    # Test 4: Empty list - should raise error
    try:
        result = average_ratios([])
        print(f"[FAIL] Test 4: Should have raised ValueError")
    except ValueError as e:
        print(f"[PASS] Test 4: Caught error gracefully - {e}")
