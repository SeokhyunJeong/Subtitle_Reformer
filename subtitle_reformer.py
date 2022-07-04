from parse import *

txt = []
with open('2_2.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        txt.append(line)

# 0: index, 1: time, 2: message
linetype = 0
stack = 0
newtime = [[]] * len(txt)
newtxt = [[]] * len(txt)
prevstart = [0, 0, 0, 0]
prevend = [0, 0, 0, 0]
index = 0
temp = ''

for line in txt:
    if line == "\t":
        break
    if linetype == 0:
        linetype = 1
    elif linetype == 1:
        stack += 1
        timestamp = parse("{}:{}:{},{} --> {}:{}:{},{}\n", line)
        start = timestamp[0:4]
        end = timestamp[4:8]
        prevend = start
        if int(start[2]) - int(prevend[2]) >= 2 or stack == 5:
            temp = ''
            stack = 0
        newtime[index] = "{}:{}:{},{} --> {}:{}:{},{}\n".format(prevstart[0],prevstart[1],prevstart[2],prevstart[3],prevend[0],prevend[1],prevend[2],prevend[3])
        #print(newtime[index], end='')
        prevstart = start
        prevend = end
        index += 1
        linetype = 2
    elif linetype == 2:
        temp = temp + line
        newtxt[index] = temp
        #print(newtxt[index+1], end='')
        prevend = start
        linetype = 3
    elif linetype == 3:
        linetype = 0
newtime[index] = "{}:{}:{},{} --> {}:{}:{},{}\n".format(prevstart[0],prevstart[1],prevstart[2],prevstart[3],end[0],end[1],end[2],end[3])

with open('2_2mod.txt', 'w') as w:
    for i in range(1, index+1):
        w.write('{}\n'.format(i))
        w.write(str(newtime[i]))
        w.write(str(newtxt[i]))
        w.write('\n')
