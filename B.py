while True:
    c = int(input('2^？（input 10n）：'))/10-1#执行次数
    y = [1,0,2,4]
    a = [1,0,2,4]
    while c > 0:
        x = a
        sx = len(x)
        sz = sx + 3
        z = [0] * sz
        i = j = 0
        while i < sx :
            while j < 4 :
                t = i + j
                z[t] = z[t] + x[i] * y[j]
                j = j + 1
            j = 0
            i = i + 1
        z.reverse()
        a = []
        r = p = q = 0
        while r < sz :
            p = z[r] + q
            q = p//10
            a.append(p%10)
            r = r + 1
        a.reverse()
        c = c - 1
    print(a)
    
    
    
    
    
    
    
    
    