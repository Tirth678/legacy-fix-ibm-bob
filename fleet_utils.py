# fleet_utils.py
# Helpers for Vossberg Mobility fleet calculations.

MILES_PER_KM = 0.621371                 # 1 km = 0.621371 miles


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a value as a whole-number percentage string."""
    return f"{int(value)}%"


def mean(values: list) -> float:
    """Return the arithmetic mean of a list, or 0 if the list is empty."""
    if not values:
        return 0
    return sum(values) / len(values)


def is_due(pct: float, threshold: float) -> bool:
    """Return True if pct has reached or exceeded threshold."""
    return pct >= threshold
