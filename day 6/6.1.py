import re
file = open("input.txt", "r")
time=re.split(" |\n|Time:",file.readline())
record=re.split(" |\n|Distance:",file.readline())
while '' in time:
    time.remove('')
while '' in record:
    record.remove('')
print('Time: ',time)
print('Record: ',record)

tot=1
for i in range(len(time)):
    print('Gara: ',i+1)
    count=0
    for j in range(1,int(time[i])+1):
        if j*(int(time[i])-j) > int(record[i]):
            count+=1

    tot=tot*count
print('Totale: ',tot)        