'''
Module
'''


def utf_len(strng: bytes) -> int:
    '''

    number of characters
    :param strng:
    :return:
    '''

    count_letter = 0
    for byte_in_line in strng:
        if byte_in_line & 0b10000000 == 0b0:
            count_letter += 1
        elif (byte_in_line & 0b01000000) == 0b1000000:
            count_letter += 1
    return count_letter

