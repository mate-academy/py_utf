"""
docstring
"""


def utf_len(string: bytes) -> int:
    """

    :param s:
    :return:
    """
    new_st = str(string)[2:-1].split()
    count = 0
    for i in range(len(new_st)):
        if '\\xd' in new_st[i]:
            # rus
            count += len(new_st[i]) // 4 // 2 + len(new_st[i]) % 4
        elif '\\xe' in new_st[i]:
            count += len(new_st[i]) // 4 // 3 + len(new_st[i]) % 4
        else:
            count += len(new_st[i])
    return count + str(string).count(' ')
