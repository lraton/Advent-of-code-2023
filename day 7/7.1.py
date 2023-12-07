file = open("input.txt", "r")
order_card=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
combination=[]
index=0
for line in file:
    temp=line.split(" ")
    combination.append(sorted(temp[0],key=order_card.index))
    tipo=1
    nome=""
    for i in range(0,len(combination[index])):
        if i+1<len(combination[index]) and combination[index][i]==combination[index][i+1]:
            if nome==combination[index][i] or nome=="":
                tipo+=1
                nome=combination[index][i]
    
    print(tipo)
    print(combination[index])
    print('\n')
    index+=1

#print(combination)