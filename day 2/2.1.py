import re
red=12
green=13
blue=14
game=1
count=0
file = open("input.txt", "r")
for line in file:
    print('game',game)
    correct=0
    sets=re.split(';|:', line)
    for i in range(len(sets)):
        if i+1<len(sets):
            color=re.split(',| |\n', sets[i+1])
            print(color)
            for j in range(len(color)):
                if color[j]=='red':
                    if int(color[j-1])>red:
                        correct=1
                        
                elif color[j]=='green':
                    if int(color[j-1])>green:
                        correct=1
                        
                elif color[j]=='blue':
                    if int(color[j-1])>blue:
                        correct=1
                        


    if correct == 0:
        count=count+game
        print('sum game',count)
    game=game+1

print('sum game',count)
    