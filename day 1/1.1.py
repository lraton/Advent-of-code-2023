f = open("input.txt", "r")
ntot=0
for x in f:
    n1=0
    n2=0

    k=list(x)
    for i in k:
        if i.isnumeric():
            n1=i
            break
            
    for i in reversed(k):
        if i.isnumeric():
            n2=i
            break

    ntot=ntot+int(str(n1) + str(n2))
    print(ntot)