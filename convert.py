"""Docstring"""
def utf_len(string: bytes) -> int:
    """

    :param string: bytes
    :return: int
    """
    counter = 0
    if string:
        print(string)
        for char in string:
            if char & 0b10000000 == 0b000 or \
                    char & 0b01000000 == 0b01000000:
                counter += 1

    return counter
