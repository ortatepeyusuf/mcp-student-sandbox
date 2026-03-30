"""
Clean code refactoring example following Python best practices:
- Single Responsibility Principle (SRP)
- Clear naming conventions
- Separation of concerns
- Testability
"""

def calculate_with_markup(value, markup_percentage=1.15):
    """Calculate value with markup applied."""
    return value * markup_percentage


def format_result(value):
    """Format result for display."""
    return f"Total: {value:.2f}"


def process_values(data):
    """Apply calculation to all values (pure function, no side effects)."""
    return [calculate_with_markup(value) for value in data]


def log_results(results, filename="log.txt"):
    """Write results to log file."""
    with open(filename, "a") as f:
        f.write(str(results) + "\n")


def display_results(results):
    """Print formatted results to console."""
    for result in results:
        print(format_result(result))


def process_data(data, log_file="log.txt", display=True):
    """
    Main orchestrator function.

    Args:
        data: List of numbers to process
        log_file: Path to log file
        display: Whether to print results to console

    Returns:
        List of processed values
    """
    processed = process_values(data)

    if display:
        display_results(processed)

    log_results(processed, log_file)

    return processed
