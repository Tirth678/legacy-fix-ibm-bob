# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: int | float, interval: int | float) -> float:
    """Return how much of the service interval has been used, as a percentage (0–100+)."""
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return True if the car has reached or exceeded the warning threshold.

    A car with no last_service_km reading is treated as recently serviced
    (last = odometer) so it is never falsely flagged.
    """
    odometer = car["odometer"]
    last = car.get("last_service_km", odometer)
    km_since = odometer - last
    return wear_percent(km_since, SERVICE_INTERVAL_KM) >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list:
    """Flag every car that needs a service and return their IDs."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
