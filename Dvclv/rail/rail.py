def i():
    inputint = int(input('_'))
    return inputint

def j():
    l = []
    v = 1
    while v != 0:
        v = i()
        v3 = v//1000
        l.append(v3)
        v2 = (v - v3)//100
        l.append(v2)
        v1 = (v3 - v2)//10
        l.append(v1)
        v0 = v2 - v1
        l.append(v0)
    l.pop(4)
    return l

x = j()
lenx = len(x)
y = j()
leny = len(y)

lenz = lenx + leny - 1
z = [0] * lenz

i = 0
j = 0
while i < lenx :
    while j < leny :
        cell = i + j
        z[cell] = z[cell] + x[i] * y[j]
        j = j + 1
    j = 0
    i = i + 1

z.reverse()

answer = []
way = 0
surface = 0
add = 0

while way < lenz :
    surface = z[way] + add
    add = surface//10
    answer.append(surface%10)
    way = way + 1

answer.reverse()

print(answer)