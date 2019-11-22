"""
docstring
"""


def utf_len(string: bytes) -> int:
    """

    :param string:
    :param s:
    :return:
    """
    b_len = sum(byte & 0b10000000 == 0b000 or byte & 0b01000000 == 0b01000000 for byte in string)
    return b_len
