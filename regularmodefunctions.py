import function
def ecnryptionregular(keyarray, inputtext):
    bintext = ""
    fullkey = ""
    resultbin = ""
    hollow = ""
    L = ""
    R = ""
    L1 = ""
    R1 = ""
    M = ""
    """
    #converting text from ascii to bin
    for i in range (len(inputtext)):
        binletter = bin(ord(inputtext[i]))[2:]
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
        bindiff = bin(int(diff / 8))[2:]
        if len(bindiff) < 8:
            m = 8 - len(bindiff)
            n = ""
            for j in range(m):
                n += "0"
            n += bindiff
            bindiff = n
        for i in range (int(diff / 8)):
            bintext += bindiff
    print(bintext)
    """
    amount = int(len(inputtext) / 64)
    textarr = []
    k0 = ""
    for j in range (64):
        k0 += inputtext[j]
    textarr.append(k0)
    print(textarr)
    #actual encryption
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
            M = function.xorfunction(R, keyarray[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (8):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, keyarray[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (8):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, keyarray[j])
            R1 = int(L, 2) ^ int(M, 2)
            L = L1
            R = R1
        for j in range (7, 0 , -1):
            R = bin(R)[2:]
            if len(R) < 32:
                m = 32 - len(R)
                n = ""
                for k in range(m):
                    n += "0"
                n += R
                R = n
            L1 = R
            M = function.xorfunction(R, keyarray[j])
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
        M = function.xorfunction(R, keyarray[0])
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
    # converting text from binary to hex
    """
    amount = int(len(resultbin) / 8)
    hexresulttext = ""
    for i in range (amount):
        binhex = ""
        for j in range (8):
            binhex += resultbin[i * 8 + j]
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
    print(hexresulttext)"""
    return(resultbin)
def decryptionregular(inputkey, inputtext):
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
    """
    decryptedtext = ""
    fraction = int(len(resultbin) / 8)
    for i in range (fraction):
        letter = ""
        for j in range (8):
            letter += resultbin[i * 8 + j]
        decryptedtext += chr(int(letter, 2))
    print(f"decrypted text is \n{decryptedtext}")
    """
    return(resultbin)