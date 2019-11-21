"""Count symbols in string"""


def utf_len(string: bytes):
    """Count symbols in string"""
    amount_symbols = 0
    for byte in string:
        if byte & 0b10000000 == 0b0 or byte & 0b01000000 == 0b1000000:
            amount_symbols += 1
    return amount_symbols
