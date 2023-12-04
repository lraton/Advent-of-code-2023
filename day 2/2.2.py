import re
red=12
green=13
blue=14
game=1
count=0
power=0
file = open("input.txt", "r")
for line in file:
    print('game',game)
    maxred=0
    maxgreen=0
    maxblue=0
    correct=0
    sets=re.split(';|:', line)
    for i in range(len(sets)):
        if i+1<len(sets):
            color=re.split(',| |\n', sets[i+1])
            print(color)
            for j in range(len(color)):
                if color[j]=='red':
                    if int(color[j-1])>maxred:
                        maxred=int(color[j-1])
                        
                elif color[j]=='green':
                    if int(color[j-1])>maxgreen:
                        maxgreen=int(color[j-1])
                        
                elif color[j]=='blue':
                    if int(color[j-1])>maxblue:
                        maxblue=int(color[j-1])

    power=power+(maxred*maxgreen*maxblue)
    game=game+1
print('sum',power)

    