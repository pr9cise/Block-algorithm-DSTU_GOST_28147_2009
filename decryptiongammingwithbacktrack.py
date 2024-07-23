import regularmodefunctions
def decryptiongammingwithbacktrack():
    InitializationVector = input(f"Введіть вектор ініціалізації (менше 18446744073709551616):\n")
    if int(InitializationVector) >= 18446744073709551616:
        print("InitializatoinVectorError!")
        exit()
    Text = input(f"Введіть текст:\n")
    Key = input(f"Введіть ключ:\n")
    fullbinvector = ""
    fullbinkey = ""
    finalbintext = ""
    K8 = []
    N1 = ""
    N2 = ""
    N = ""
    #checking vector for compatibility
    if len(bin(int(InitializationVector))[2:]) < 64:
        m = 64 - len(bin(int(InitializationVector))[2:])
        n = ""
        for i in range(m):
            n += "0"
        n += bin(int(InitializationVector))[2:]
        fullbinvector = n
    else:
        fullbinvector = bin(int(InitializationVector))[2:]
    print(f"fullbinvector = {fullbinvector}")
    #checking key for compatibility
    if len(bin(int(Key))[2:]) < 256:
        m = 256 - len(bin(int(Key))[2:])
        n = ""
        for i in range(m):
            n += "0"
        n += bin(int(Key))[2:]
        fullbinkey = n
    else:
        fullbinkey = bin(int(Key))[2:]
    print(fullbinkey)
    for i in range(8):
        k0 = ""
        for j in range(32):
            k0 += fullbinkey[i * 32 + j]
        K8.append(k0)
    print(K8)
    #converting text from hex to bin
    fraction = int(len(Text) / 3)
    bintext = ""
    fullbit = ""
    for i in range (fraction):
        hex1 = Text[i * 3] + Text[i * 3 + 1]
        print(f"hex = {hex1}")
        bit = bin(int(hex1, 16))[2:]
        if len(bit) < 8:
            m = 8 - len(bit)
            n = ""
            for i in range(m):
                n += "0"
            n += bit
            fullbit = n
        else:
            fullbit = bit
        bintext += fullbit
    print(f"bintext\n{bintext}")
    print(len(bintext))
    #actual decryption
    value1 = int(len(bintext) / 64)
    N1 = fullbinvector[:32]
    N2 = fullbinvector[32:]
    N1N2 = N1 + N2
    for i in range (value1):
        textpart = ""
        for j in range (64):
            textpart += bintext[i * 64 + j]
        textencr = regularmodefunctions.ecnryptionregular(K8, N1N2)
        inttextencr = int(textencr, 2)
        inttextpart = int(textpart, 2)
        xoredtext = inttextpart ^ inttextencr
        if len(bin(xoredtext)[2:]) < 64:
            m = 64 - len(bin(xoredtext)[2:])
            n = ""
            for i in range(m):
                n += "0"
            n += bin(xoredtext)[2:]
            xoredbintext = n
        else:
            xoredbintext = bin(xoredtext)[2:]
        finalbintext += xoredbintext
        N1N2 = textpart
    print(f"finalbintext\n{finalbintext}")
    #converting from bin to ascii
    decryptedtext = ""
    fraction = int(len(finalbintext) / 8)
    for i in range (fraction):
        letter = ""
        for j in range (8):
            letter += finalbintext[i * 8 + j]
        decryptedtext += chr(int(letter, 2))
    print(f"decrypted text is \n{decryptedtext}")