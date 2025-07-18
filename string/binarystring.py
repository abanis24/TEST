import re

def check_binary_string(s):
    # char_set = {'0','1'}
    # str_set = set(s)

    # if str_set == char_set or str_set == {'0'} or str_set == {'1'}:
    #     print('Yes, the string is binary')
    # else:
    #     print('nO')

    # t = '01'
    # if all((letter in t) for letter in s):
    #     print('yes')
    # else:
    #     print('no')

    regex = r"[^01]"

    if re.search(pattern=regex,string=s):
        return False
    else:
        return True

str = "010101"
print(check_binary_string(str))