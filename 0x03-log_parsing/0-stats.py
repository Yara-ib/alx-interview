#!/usr/bin/python3
""" Log parsing Module """
import re
import signal
from types import FrameType
import sys


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

size_total = 0
lines_printed = 0

# The regex to get the matching data needed
log = re.compile(
    r'^(\S+)' # Group 1: Match IP
    r' - '
    r'\[.*?\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3})' # Group 2
    r' (\d+)$'  # Group 3
)


def stats() -> str:
    """
    Prints the stats saved

    Returns:
        str: <status code>: <number>
    """

    print(f"File size: {size_total}")
    for status in sorted(status_codes.keys()):
        if status_codes[status] > 0:
            print(f"{status}: {status_codes[status]}")


def catch_signal(signal: int, frame: FrameType) -> None:
    """
    Catches if any interruption signal been used

    Args:
        signal (int): signal number that caused the interrupt
        frame (FrameType): program's state at time of the signal
    """
    stats()
    sys.exit(0)


# trying to apply it
signal.signal(signal.SIGINT, catch_signal)

# Can't be added, causes error
# signal.signal(signal.SIGKILL, catch_signal)

try:
    for line in sys.stdin:
        line = line.strip()
        matched_data = log.match(line)
        if matched_data:
            # Getting the data using regex
            status = int(matched_data.group(2))
            size_file = int(matched_data.group(3))

            size_total += size_file
            if status in status_codes:
                status_codes[status] += 1

            lines_printed += 1

            # Printing the stats each 10 lines as required
            if lines_printed % 10 == 0:
                stats()

except Exception as e:
    pass

stats()
