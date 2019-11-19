"""len module"""


def utf_len(string: bytes) -> int:
    """len function"""
    return len(str(string, 'utf-8'))
