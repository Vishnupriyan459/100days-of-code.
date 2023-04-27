chipertext = []
chiperstring = input("Enter the ciphertext: ")
for character in chiperstring:
    chipertext.append(character)

def checker(ciphertext):
    firsttxt = []
    secondtxt = []
    if len(ciphertext) % 2 != 0:
        limit = (len(ciphertext) // 2) + 1
    elif len(ciphertext) % 2 == 0:
        limit = (len(ciphertext) // 2)
    # checker
    for i in range(limit):
        firsttxt.append(ciphertext[i])
    for i in range(limit, len(ciphertext)):
        secondtxt.append(ciphertext[i])
    # plaintext
    plaintext = []
    if len(ciphertext) % 2 != 0:
        for i in range(len(secondtxt)):
            plaintext.append(firsttxt[i])
            plaintext.append(secondtxt[i])
        return plaintext
    elif len(ciphertext) % 2 == 0:
        for i in range(len(firsttxt)):
            plaintext.append(firsttxt[i])
            plaintext.append(secondtxt[i])
        return plaintext
print("The plaintext: ")
print("".join(checker(chipertext)))

                  
                  
