import encryptionregular
import decryptionregular
import encryptiongamming
import decryptiongamming
import encryptiongammingwithbacktrack
import decryptiongammingwithbacktrack
choice1 = input("Введіть функцію (1 - шифрування; 2 - дешифрування): ")
choice2 = input("Введіть режим (1 - простої заміни; 2 - гамування; 3 - гамування зі зворотним зв'язком): ")
if choice1 == "1":
    if choice2 == "1":
        encryptionregular.encryptionregular()
    elif choice2 == "2":
        encryptiongamming.encryptiongamming()
    elif choice2 == "3":
        encryptiongammingwithbacktrack.encryptiongammingwithbacktrack()
    else:
        print("InputError!")
elif choice1 == "2":
    if choice2 == "1":
        decryptionregular.decryptionregular()
    elif choice2 == "2":
        decryptiongamming.decryptiongamming()
    elif choice2 == "3":
        decryptiongammingwithbacktrack.decryptiongammingwithbacktrack()
    else:
        print("InputError!")
else:
    print("InputError!")