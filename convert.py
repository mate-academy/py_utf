"""len module"""


def utf_len(string: bytes) -> int:
    """len function"""
    # прибираємо лишні знаки
    string_without_odd = str(string)[2:-1]
    result = 0
    index = 0
    while index <= len(string_without_odd)-1:
        result += 1
        # вичисляємо кирилицю
        if string_without_odd[index:index+3] == "\\xd":
            index += 8
        # вичисляємо китайщину
        elif string_without_odd[index:index+3] == "\\xe":
            index += 12
        else:
            index += 1
    return result
