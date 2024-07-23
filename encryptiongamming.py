import regularmodefunctions
import math
def encryptiongamming():
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
    N3 = ""
    N4 = ""
    N1 = ""
    N2 = ""
    C1 = "00000001000000010000000100000100"
    C2 = "00000001000000010000000100000001"
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
    #using function
    print(f"using standart file")
    N = regularmodefunctions.ecnryptionregular(K8, fullbinvector)
    N3 = N[:32]
    N4 = N[32:]
    print(f"N3\n{N3}\nN4\n{N4}")
    #converting text from ascii to bin
    bintext = ""
    for i in range (len(Text)):
        binletter = bin(ord(Text[i]))[2:]
        fullbinletter = ""
        if len(binletter) < 8:
            m = 8 - len(binletter)
            n = ""
            for j in range(m):
                n += "0"
            n += binletter
            fullbinletter = n
        else:
            fullbinletter = binletter
        bintext += fullbinletter
    if len(bintext) % 64 != 0:
        diff = 64 - (len(bintext) % 64)
        print(diff)
        for i in range (diff):
            bintext += "0"
    print(bintext)
    #actual encryption
    value1 = int(len(bintext) / 64)
    for i in range (value1):
        textpart = ""
        for j in range (64):
            textpart += bintext[i * 64 + j]
        intN3 = int(N3, 2)
        intN4 = int(N4, 2)
        intC = int(C2, 2)
        xorN3 = intN3 ^ intC
        intC = int(C1, 2)
        xorN4 = intN4 ^ intC
        if len(bin(xorN3)[2:]) < 32:
            m = 32 - len(bin(xorN3)[2:])
            n = ""
            for i in range(m):
                n += "0"
            n += bin(xorN3)[2:]
            N3 = n
        else:
            N3 = bin(xorN3)[2:]
        if len(bin(xorN4)[2:]) < 32:
            m = 32 - len(bin(xorN4)[2:])
            n = ""
            for i in range(m):
                n += "0"
            n += bin(xorN4)[2:]
            N4 = n
        else:
            N4 = bin(xorN4)[2:]
        N3N4 = N3 + N4
        print(f"N3\n{N3}\nN4\n{N4}\nresult\n{N3N4}")
        textencr = regularmodefunctions.ecnryptionregular(K8, N3N4)
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
    print(f"finalbintext\n{finalbintext}")
    #converting text form bin to hex
    amount = int(len(finalbintext) / 8)
    hexresulttext = ""
    for i in range (amount):
        binhex = ""
        for j in range (8):
            binhex += finalbintext[i * 8 + j]
        print(binhex)
        hexoutputtext = hex(int(binhex, 2))[2:]
        fullhex1 = ""
        if len(hexoutputtext) < 2:
            m = 2 - len(hexoutputtext)
            n = ""
            for i in range(m):
                n += "0"
            n += hexoutputtext
            fullhex1 = n
        else:
            fullhex1 = hexoutputtext
        print(fullhex1)
        hexresulttext += fullhex1 + " "
    print(hexresulttext)