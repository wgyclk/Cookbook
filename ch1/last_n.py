exemple=[1324,1324,5,15566,89467,9,637,2456,584,245]
print(exemple)
from collections import deque
a=deque()
print(a)
def last_n(n):
    global a
    a=deque(maxlen=n)
    for i in exemple:
        a.append(i)
    print(a)
last_n(5)
print(a)
