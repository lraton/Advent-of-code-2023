f = open("input.txt", "r")
ntot=0
search_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for x in f:
    print('nuova linea')
    n1=0
    n2=0
    position=[]
    whatnumber=[]
    positionsorted=[]
    whatnumbersorted=[]
    #find position idgit
    for i in range(len(search_words)):
        find=x.find(search_words[i])
        if find!=-1:
            position.append(find)
            whatnumber.append(search_words[i])
    
    for i in range(len(position)):
        positionsorted.append(position[i])
        whatnumbersorted.append(whatnumber[i])
        if position[i]<positionsorted[0]:
            positionsorted.insert(0,position[i])
            whatnumbersorted.insert(0,whatnumber[i])

    print(position)
    print(whatnumber)

    #find first and last number
    k=list(x)
    for i in range(len(k)):
        if k[i].isnumeric():
            if i<len(k)-1 and position:
                if i>position[0]:
                    #n1=whatnumber[0]
                    break
            n1=k[i]
            break
            
    for i in reversed(range(len(k))):
        if k[i].isnumeric():
            if i>0 and position:
                if i<position[len(position)-1] :
                    #n2=whatnumber[len(whatnumber)-1]
                    break
            n2=k[i]
            break

    ntot=ntot+int(str(n1) + str(n2))
    print(ntot)
