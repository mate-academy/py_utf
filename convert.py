"""len module"""


def utf_len(string: bytes) -> int:
    """len function"""
    result = 0
    for byte in string:
        if (byte & 0b10000000) == 0b000:
            result += 1
        elif (byte & 0b01000000) == 0b1000000:
            result += 1
    return result
