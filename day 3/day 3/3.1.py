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
        if matrice[i][j].isnumeric():
            inizio=j
            if i>0 and j>0 and  not matrice[i-1][j-1].isnumeric() and not matrice[i-1][j-1] =='.':
                res=1 #1 è corretto, 0 è sbagliato
            if j>0 and not matrice[i][j-1].isnumeric() and  not matrice[i][j-1] =='.':
                res=1
            if i+1<len(matrice) and j>0 and not matrice[i+1][j-1].isnumeric() and not matrice[i+1][j-1] =='.':
                res=1
               

            while matrice[i][j].isnumeric():
                if i>0 and not matrice[i-1][j].isnumeric() and not matrice[i-1][j] =='.':
                    res=1
                if i+1<len(matrice) and not matrice[i+1][j].isnumeric() and not matrice[i+1][j] =='.' :
                    res=1

                numero=str(numero)+str(matrice[i][j])

                if j+1<len(matrice[i]):
                    j+=1
                else:
                    break

            if i>0 and not matrice[i-1][j].isnumeric() and not matrice[i-1][j] =='.':
                res=1 #1 è corretto, 0 è sbagliato
            if not matrice[i][j].isnumeric() and not matrice[i][j] =='.':
                res=1
            if i+1<len(matrice) and not matrice[i+1][j].isnumeric() and not matrice[i+1][j] =='.' :
                res=1

            if res==1:
                contatore=contatore+int(numero)
                print(numero)
        j+=1
print (contatore)