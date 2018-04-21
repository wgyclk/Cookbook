a=[['a','b','c','d','e'],[1,2,3,4,5],[6,7,8,9,10]]
print(a)
print(a[1][0])
b=dict()
c=dict()
d=[]
la=len(a[1])
for i in range(len(a[0])):
    b[a[0][i]]=a[1][i]
    c[a[0][i]]=a[2][i]
d.append(b)
d.append(c)
print(d)
    
    
        


        
    
        
    
    

