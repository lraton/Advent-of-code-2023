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

for i in range(0,len(matrice)):
    j=0
    while j in range(0,len(matrice[i])):
        res=0
        numero=''
        numeri=[]
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
                inizio=tempj
                numero=str(numero)+str(matrice[i-1][inizio])
                while matrice[i-1][tempj+1].isnumeric():
                    numero=str(numero)+str(matrice[i-1][tempj+1])
                    if tempj+1<len(matrice[i]):
                        tempj+=1
                    else:
                        break
                fine=tempj
                print(numero)

                if fine<j:
                    #controllo j+1 e nel caso ho il secondo numero
                    tempj=j
                    numero=''
                    if j+1<len(matrice[i]) and i>0 and matrice[i-1][j+1].isnumeric():
                        inizio=tempj
                        while matrice[i-1][tempj+1].isnumeric():
                            numero=str(numero)+str(matrice[i-1][tempj+1])
                            if tempj+1<len(matrice[i]):
                                tempj+=1
                            else:
                                break
                        fine=tempj
                        print(numero)

            else:
                #controllo j, e seguito, soltanto
                if i>0 and matrice[i-1][j].isnumeric():
                    tempj=j
                    numero=''
                    while matrice[i-1][tempj].isnumeric():
                        numero=str(numero)+str(matrice[i-1][tempj])
                        if tempj+1<len(matrice[i]):
                            tempj+=1
                        else:
                            break
                    fine=tempj
                    print(numero)
                    if fine<j+1:
                        if i>0 and j+1<len(matrice[i]) and matrice[i-1][j+1].isnumeric():
                            tempj=j
                            numero=''
                            while matrice[i-1][tempj+1].isnumeric():
                                numero=str(numero)+str(matrice[i-1][tempj+1])
                                if tempj+1<len(matrice[i]):
                                    tempj+=1
                                else:
                                    break
                            fine=tempj
                            print(numero)
                else:                 
                    #controllo j+1
                    tempj=j
                    numero=''
                    if i>0 and j+1<len(matrice[i])and matrice[i-1][j+1].isnumeric():
                        while matrice[i-1][tempj+1].isnumeric():
                            numero=str(numero)+str(matrice[i-1][tempj+1])
                            if tempj+1<len(matrice[i]):
                                tempj+=1
                            else:
                                break
                        fine=tempj
                        print(numero)

            #sotto
            numero=''
            tempj=j
            if j>0 and i+1<len(matrice) and matrice[i+1][j-1].isnumeric():
                while matrice[i+1][tempj-1].isnumeric():
                    if tempj-1>=0:
                        tempj-=1
                    else:
                        break
                inizio=tempj
                numero=str(numero)+str(matrice[i+1][inizio])
                while matrice[i+1][tempj+1].isnumeric():
                    numero=str(numero)+str(matrice[i+1][tempj+1])
                    if tempj+1<len(matrice[i]):
                        tempj+=1
                    else:
                        break
                fine=tempj
                print(numero)

                if fine<j:
                    #controllo j+1 e nel caso ho il secondo numero
                    tempj=j
                    numero=''
                    if j+1<len(matrice[i]) and i<len(matrice) and matrice[i+1][j+1].isnumeric():
                        inizio=tempj
                        while matrice[i+1][tempj+1].isnumeric():
                            numero=str(numero)+str(matrice[i+1][tempj+1])
                            if tempj+1<len(matrice[i]):
                                tempj+=1
                            else:
                                break
                        fine=tempj
                        print(numero)

            else:
                #controllo j, e seguito, soltanto
                if i+1<len(matrice) and matrice[i+1][j].isnumeric():
                    tempj=j
                    numero=''
                    while matrice[i+1][tempj].isnumeric():
                        numero=str(numero)+str(matrice[i+1][tempj])
                        if tempj+1<len(matrice[i]):
                            tempj+=1
                        else:
                            break
                    fine=tempj
                    print(numero)
                    if fine<j+1:
                        if i<len(matrice) and j+1<len(matrice[i]) and matrice[i+1][j+1].isnumeric():
                            tempj=j
                            numero=''
                            while matrice[i+1][tempj+1].isnumeric():
                                numero=str(numero)+str(matrice[i+1][tempj+1])
                                if tempj+1<len(matrice[i]):
                                    tempj+=1
                                else:
                                    break
                            fine=tempj
                            print(numero)
                else:                 
                    #controllo j+1
                    if i+1<len(matrice) and j+1<len(matrice[i]) and matrice[i+1][j+1].isnumeric():
                            tempj=j
                            numero=''
                            while matrice[i+1][tempj+1].isnumeric():
                                numero=str(numero)+str(matrice[i+1][tempj+1])
                                if tempj+1<len(matrice[i]):
                                    tempj+=1
                                else:
                                    break
                            fine=tempj
                            print(numero)

            #destra   
            if j+1<len(matrice[i]) and matrice[i][j+1].isnumeric():
                res=1

          
        j+=1