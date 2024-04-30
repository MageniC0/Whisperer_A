def i():
    u = int(input('_'))
    return u

def j():
    l = []
    v = 1
    while v != 0:
        v = i()
        v0 = v%10
        v1 = (v//10)%10
        v2 = (v//100)%10
        v3 = v//1000
        l.append(v3)
        l.append(v2)
        l.append(v1)
        l.append(v0)
    l.pop()
    l.pop()
    l.pop()
    l.pop()
    return l

x = j()
sx = len(x)
y = j()
sy = len(y)

sz = sx + sy - 1
z = [0] * sz

i = 0
j = 0
while i < sx :
    while j < sy :
        t = i + j
        z[t] = z[t] + x[i] * y[j]
        j = j + 1
    j = 0
    i = i + 1

z.reverse()

a = []
r = 0
p = 0
q = 0

while r < sz :
    p = z[r] + q
    q = p//10
    a.append(p%10)
    r = r + 1

a.reverse()

print(a)















