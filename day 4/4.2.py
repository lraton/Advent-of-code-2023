import re
file = open("input.txt", "r")
cardn=1
somma=0
for line in file:
    cards=[]
    vincenti=[]
    mieinumeri=[]
    cards=line.split('|')
    stringa='Card '+ str(cardn) +': '
    vincenti=cards[0].split(stringa)
    mieinumeri=cards[1].split('\n')
    while'' in vincenti:
        vincenti.remove('')
    while'' in mieinumeri:
        mieinumeri.remove('')

    vincentin=vincenti[0].split(' ')
    mieinumerin=mieinumeri[0].split(' ')
    while'' in vincentin:
        vincentin.remove('')
    while'' in mieinumerin:
        mieinumerin.remove('')


    count=0
    for i in range(len(mieinumerin)):
        for j in range(len(vincentin)):
            if mieinumerin[i]==vincentin[j]:
                count+=1


    print('Vincenti ',vincentin)
    print('Miei numeri ',mieinumerin)
    print('Count ',count)
    
    cardn=cardn+1