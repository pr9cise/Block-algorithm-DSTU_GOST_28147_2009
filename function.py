Sbox = [
    [10, 9, 13, 6, 14, 11, 4, 5, 15, 1, 3, 12, 7, 0, 8, 2],
    [8, 0, 12, 4, 9, 6, 7, 11, 2, 3, 1, 15, 5, 14, 10, 13],
    [15, 6, 5, 8, 14, 11, 10, 4, 12, 0, 3, 7, 2, 9, 1, 13],
    [3, 8, 13, 9, 6, 11, 15, 0, 2, 5, 12, 10, 4, 14, 1, 7],
    [15, 8, 14, 9, 7, 2, 0, 13, 12, 6, 1, 5, 11, 4, 3, 10],
    [2, 8, 9, 7, 5, 15, 0, 11, 12, 1, 13, 14, 10, 3, 6, 4],
    [3, 8, 11, 5, 6, 4, 14, 10, 2, 12, 1, 7, 9, 15, 13, 0],
    [1, 2, 3, 14, 6, 13, 11, 8, 15, 10, 12, 5, 7, 9, 0, 4]
]
def xorfunction(inputtext, inputkey):
    print(f"inputtext = {inputtext}")
    print(f"inputkey = {inputkey}")
    bin_text = int(inputtext, 2)
    bin_key = int(inputkey, 2)
    print(f"bin_text = {bin_text}")
    print(f"bin_key = {bin_key}")
    xor_result = bin_text ^ bin_key
    print(f"xor_result = {xor_result}")
    bin_result = bin(xor_result)[2:]
    fullbin = ""
    if len(bin_result) < 32:
        m = 32 - len(bin_result)
        n = ""
        for i in range(m):
            n += "0"
        n += bin_result
        fullbin = n
    else:
        fullbin = bin_result
    print(fullbin)
    textarray = []
    for i in range (8):
        part = fullbin[i * 4] + fullbin[i * 4 + 1] + fullbin[i * 4 + 2] + fullbin[i * 4 + 3]
        textarray.append(int(part, 2))
    print(textarray)
    for i in range (8):
        textarray[i] = Sbox[i][int(textarray[i])]
    print(textarray)
    encrypted = ""
    for i in range (8):
        if len(bin(textarray[i])[2:]) < 4:
            m = 4 - len(bin(textarray[i])[2:])
            n = ""
            for j in range(m):
                n += "0"
            n += bin(textarray[i])[2:]
            fulltext = n
        else:
            fulltext = bin(textarray[i])[2:]
        encrypted += fulltext
    print(encrypted)
    result = encrypted[11:] + encrypted[:11]
    print(f"result = {result}")
    return (result)