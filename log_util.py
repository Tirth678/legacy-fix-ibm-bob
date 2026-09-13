# log_util.py
# Homemade logger for Vossberg Mobility nightly runs.

import time

LOG_LINES: list[str] = []               # module-level buffer, flushed to disk by flush_log


def log(message: str) -> None:
    """Append a timestamped message to the in-memory buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write all buffered lines to the log file and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
