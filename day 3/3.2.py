file = open("input.txt", "r")
contatore=0
matrice=[]
for line in file:
    linee=[]
    for i in line:
        linee.append(i)
        if i == '\n':
            linee.pop()
    matrice.append(linee)        
print(matrice)

for i in range(0,len(matrice)):
    j=0
    while j in range(0,len(matrice[i])):
        res=0
        numero=''
        if matrice[i][j]=='*':
            #sinistra
            if j>0 and matrice[i][j-1].isnumeric():
                res=1

            #sopra
            tempj=j
            if j>0 and i>0 and matrice[i-1][j-1].isnumeric():
                while matrice[i-1][tempj-1].isnumeric():
                    if tempj-1>=0:
                        tempj-=1
                    else:
                        break
                inizio=j+1
                while matrice[i-1][tempj].isnumeric():
                    if tempj+1<len(matrice[i]):
                        tempj+=1
                    else:
                        break
                fine=tempj

            if tempj+1<j+1:
                j=tempj+1
                if i>0 and matrice[i-1][j].isnumeric():
                    res=1
            
            if i>0 and j+1<len(matrice[i]) and matrice[i-1][j+1].isnumeric():
                    res=1

            #sotto
            if i+1<len(matrice) and j+1<len(matrice[i]) and matrice[i+1][j+1].isnumeric():
                res=1
            if i+1<len(matrice) and matrice[i+1][j].isnumeric():
                res=1
            if i+1<len(matrice) and j>0 and matrice[i+1][j-1].isnumeric():
                res=1

            #destra   
            if j+1<len(matrice[i]) and matrice[i][j+1].isnumeric():
                res=1

          
        j+=1
print (contatore)