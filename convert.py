"""
function utf_len which decode string and get its length
"""
def utf_len(encoded_string: bytes) -> int:
    """

    :param encoded_string: encoded string
    :return: length of decoded string
    """
    return len(encoded_string.decode())
