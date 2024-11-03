#!/usr/bin/python3
""" UTF-8 Validation Module """
import re


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    one_byte = re.compile(r"^0[01]{7}$")
    two_byte = re.compile(r"^110[01]{5}$")
    three_byte = re.compile(r"^1110[01]{4}$")
    four_byte = re.compile(r"^11110[01]{3}$")
    more_bytes = re.compile(r"^10[01]{6}$")

    count_bytes = 0

    for value in data:
        binary = format(value & 0xFF, "08b")

        if count_bytes == 0:
            if one_byte.match(binary):
                continue
            elif two_byte.match(binary):
                count_bytes = 1
            elif three_byte.match(binary):
                count_bytes = 2
            elif four_byte.match(binary):
                count_bytes = 3
            else:
                return False
        else:
            if not more_bytes.match(binary):
                return False
            count_bytes -= 1

    return count_bytes == 0
