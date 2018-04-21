a=[['a','b','c','d','e'],[1,2,3,4,5],[6,7,8,9,10]]
print(a)
print(a[1][0])
b=dict()
c=dict()
d=[]
la=len(a[1])
for J in a[0]:
        i=0
        b[J]=a[1][i]
        i+=1
for J in a[0]:
        i=0
        c[J]=a[2][i]
        i+=1
d.append(b)
d.append(c)
print(d)


        
    
        
    
    

