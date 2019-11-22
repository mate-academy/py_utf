def utf_len(phrase: bytes) -> int:
    counter = 0
    if phrase:
        for i in phrase:
            if 0b10000000 & i == 0b0000000 or 0b01000000 & i == 0b1000000:
                counter += 1
    return counter


