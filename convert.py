'''
Module
'''

LENGTH_BYTE_IN_STR = 10


def utf_len(strng: bytes) -> int:
    '''

    number of characters
    :param strng:
    :return:
    '''
    count_letter = 0
    for byte_in_line in strng:
        # length of the string( byte which is represented in binary form)
        lngth_binr_byte = len(str(bin(byte_in_line)))
        if lngth_binr_byte != LENGTH_BYTE_IN_STR:
            count_letter += 1
        else:
            bit = str(bin(byte_in_line)[3])
            if bit == '1':
                count_letter += 1
    return count_letter
