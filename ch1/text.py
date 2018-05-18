def triangle():
    yield [x for x in ' '*10]+['1']+[x for x in ' '*10]
    yield [x for x in ' '*9]+['1',' ','1']+[x for x in ' '*9]
    yield [x for x in ' '*8]+['1',' ','2',' ','1']+[x for x in ' '*8]
    yield [x for x in ' '*7]+['1',' ','3',' ','3',' ','1']+[x for x in ' '*7]
    yield [x for x in ' '*6]+['1',' ','4',' ','6',' ','4',' ','1']+[x for x in ' '*6] 
    yield [x for x in ' '*5]+['1',' ','5',' ','10',' ','10',' ','5',' ','1']+[x for x in ' '*5]    
a=triangle()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))




