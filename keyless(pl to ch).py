plaintxt=input("Enter the plain text:")
firsttxt=plaintxt[0]
secondtxt=""
chiphertxt=""
i=1
while(i<=len(plaintxt)-1):
    if(i%2==0):
        firsttxt+=plaintxt[i]
    else:
        secondtxt+=plaintxt[i]
    i=i+1
chiphertxt=firsttxt+secondtxt
print("The chiper text is:",chiphertxt)


