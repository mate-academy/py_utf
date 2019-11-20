"""doc"""


def utf_len(string: bytes) -> int:
    """convert"""
    count = 0
    for byte in string:
        # ascii chars
        if byte & 0b10000000 == 0b000:
            count += 1
        # others
        elif byte & 0b01000000 == 0b01000000:
            count += 1

    return count
