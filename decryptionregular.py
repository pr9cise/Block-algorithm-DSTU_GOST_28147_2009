import function
def decryptionregular():
    inputtext = input("Введіть текст:\n")
    inputkey = input("Введіть ключ:\n")
    inputkey = int(inputkey)
    bintext = ""
    fullkey = ""
    resultbin = ""
    hollow = ""
    K8 = []
    L = ""
    R = ""
    L1 = ""
    R1 = ""
    M = ""
    #checking key for compatibility
    if len(bin(inputkey)[2:]) < 256:
        m = 256 - len(bin(inputkey)[2:])
        n = ""
        for i in range(m):
            n += "0"
        n += bin(inputkey)[2:]
        fullkey = n
    elif len(bin(inputkey)[2:]) == 256:
        fullkey = bin(inputkey)[2:]
    else:
        m = len(bin(inputkey)[2:]) - 256
        fullkey = bin(inputkey)[2 + m:]
    print(fullkey)
    for i in range (8):
        k0 = ""
        for j in range (32):
            k0 += fullkey[i * 32 + j]
        K8.append(k0)
    print(K8)
    #converting text from hex to bin
    fraction = int(len(inputtext) / 3)
    bintext = ""
    fullbit = ""
    for i in range (fraction):
        hex1 = inputtext[i * 3] + inputtext[i * 3 + 1]
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
    amount = int(len(bintext) / 64)
    textarr = []
    for i in range (amount):
        k0 = ""
        for j in range (64):
            k0 += bintext[i * 64 + j]
        textarr.append(k0)
    print(f"textarr = {textarr}")
    #actual decryption
    for i in range (amount):
        partedtext = textarr[i]
        finalbin = ""
        print(f"partedtext = {partedtext}")
        L = partedtext[:32]
        R = partedtext[32:]
        for j in range (8):
            if j > 0:
                R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, K8[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (7, -1, -1):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, K8[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (7, -1, -1):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, K8[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (7, 0, -1):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, K8[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        R = bin(R)[2:]
        if len(R) < 32:
            m = 32 - len(R)
            n = ""
            for j in range(m):
                n += "0"
            n += R
            R = n
        M = function.xorfunction(R, K8[0])
        L = int(L, 2) ^ int(M, 2)
        L = bin(L)[2:]
        if len(L) < 32:
            m = 32 - len(L)
            n = ""
            for j in range(m):
                n += "0"
            n += L
            L = n
        print(f"L = {L}\nR = {R}")
        finalbin = L + R
        print(f"finalbin = {finalbin}\n////////////////////////////////////////////////")
        resultbin += finalbin
    print(len(resultbin))
    print(resultbin)
    # converting text from binary to char
    decryptedtext = ""
    fraction = int(len(resultbin) / 8)
    for i in range (fraction):
        letter = ""
        for j in range (8):
            letter += resultbin[i * 8 + j]
        decryptedtext += chr(int(letter, 2))
    print(f"decrypted text is \n{decryptedtext}")