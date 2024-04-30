c = 1
s = [0, 0, 0, 0, 0 ]
j = [0, 0, 0, 0 ]
x = [0, 0 ]
y = [0, 0 ]
v = int(input(f"_define view:"))
print(f"_define template.top.x:0")
s[0] = int(input(f"_define template.top.y:"))
s[1] = int(input(f"_define template.left.x:"))
s[2] = int(input(f"_define template.right.x:"))
s[3] = int(input(f"_define template.left.y:"))
s[4] = int(input(f"_define template.right.y:"))
class D(object):
    def __init__(self, x, y, z ):
        self.x = x
        self.y = y
        self.z = z
class E(object):
    def __init__(self, x, yl, yh ):
        self.x = x
        self.yl = yl
        self.yh = yh
P = D(0, 0, 0 )
Q = D(0, 0, 0 )
w1 = E(0, 0, 0 )
w2 = E(0, 0, 0 )
w3 = E(0, 0, 0 )
w4 = E(0, 0, 0 )
def d(d1, d2, d3, d4 ):
    d = d1 * d2 + d3 * d4
    return d
print(f"_rake on")
print(f"_version: indev PE 0.6")
print(f"_mode[1]:move point")
print(f"_mode[2]:expand point")
while c>0 :
    
    t = str(input(f"_select mode:"))
    
    if t == "1":
        
        print(f"_locate block %d:"%(c))
        P.x = int(input(f"point0.x:"))
        P.y = int(input(f"point0.y:"))
        P.z = int(input(f"point0.z:"))
        
        print(f"_locate block %d:"%(c))
        Q.x = int(input(f"move.x:"))
        Q.y = int(input(f"move.y:"))
        Q.z = int(input(f"move.z:"))
        
        x[0] = P.x
        x[1] = P.x + Q.x
        
        y[0] = P.y
        y[1] = P.y + Q.y
        
        j[0] = d(x[0],s[1],y[0],s[2])
        j[1] = d(x[0],s[3],y[0],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w1.x = v * j[0]
        w1.yl = v * j[2]
        w1.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w1.x,w1.yl,w1.yh))
        
        j[0] = d(x[1],s[1],y[0],s[2])
        j[1] = d(x[1],s[3],y[0],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w2.x = v * j[0]
        w2.yl = v * j[2]
        w2.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w2.x,w2.yl,w2.yh))
        
        j[0] = d(x[0],s[1],y[1],s[2])
        j[1] = d(x[0],s[3],y[1],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w3.x = v * j[0]
        w3.yl = v * j[2]
        w3.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w3.x,w3.yl,w3.yh))
        
        j[0] = d(x[1],s[1],y[1],s[2])
        j[1] = d(x[1],s[3],y[1],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w4.x = v * j[0]
        w4.yl = v * j[2]
        w4.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w4.x,w4.yl,w4.yh))
    
    if t == "2":
            
        print(f"_locate block %d:"%(c))
        P.x = int(input(f"point1.x:"))
        P.y = int(input(f"point1.y:"))
        P.z = int(input(f"point1.z:"))
        
        print(f"_locate block %d:"%(c))
        Q.x = int(input(f"point2.x:"))
        Q.y = int(input(f"point2.y:"))
        Q.z = int(input(f"point2.z:"))
        
        x[0] = P.x
        x[1] = Q.x
        
        y[0] = P.y
        y[1] = Q.y
        
        j[0] = d(x[0],s[1],y[0],s[2])
        j[1] = d(x[0],s[3],y[0],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w1.x = v * j[0]
        w1.yl = v * j[2]
        w1.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w1.x,w1.yl,w1.yh))
        
        j[0] = d(x[1],s[1],y[0],s[2])
        j[1] = d(x[1],s[3],y[0],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w2.x = v * j[0]
        w2.yl = v * j[2]
        w2.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w2.x,w2.yl,w2.yh))
        
        j[0] = d(x[0],s[1],y[1],s[2])
        j[1] = d(x[0],s[3],y[1],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w3.x = v * j[0]
        w3.yl = v * j[2]
        w3.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w3.x,w3.yl,w3.yh))
        
        j[0] = d(x[1],s[1],y[1],s[2])
        j[1] = d(x[1],s[3],y[1],s[4])
        j[2] = d(j[1],1,P.z,s[0])
        j[3] = d(j[2],1,Q.z,s[0])
        w4.x = v * j[0]
        w4.yl = v * j[2]
        w4.yh = v * j[3]
        print(f"[%d]: %d~%d"%(w4.x,w4.yl,w4.yh))
        
    else:
        print(f"_start with '1' or '2'")
        continue
