from bidict import bidict
td=bidict({1:'a','2':'b'})
print(td[1])
def arabic_to_roman(arabic):
    romans = list(integers)
    str_arabic = arabic[::-1]
    str_arabic_len = len(str_arabic)
    result = str()
    romans_pointer = 0
    for i in range(str_arabic_len):
        if str_arabic[i] in ['0', '1', '2', '3']:
            result = romans[romans_pointer] * int(str_arabic[i]) + result
        elif str_arabic[i] in ['4']:
            result = romans[romans_pointer] + romans[romans_pointer + 1] + result
        elif str_arabic[i] in ['5', '6', '7', '8']:
            result = romans[romans_pointer + 1] + romans[romans_pointer] * (int(str_arabic[i]) - 5) + result
        elif str_arabic[i] in ['9']:
            result = romans[romans_pointer] + romans[romans_pointer + 2] + result
        romans_pointer += 2
    return 
