exemple=[1134,45245,134,3,346,1457,9870,467,769,1,34]
import heapq
def est(n):
    b=heapq.nlargest(n,exemple)
    heapq.heapify(exemple)
    print(exemple)
est(3)
    
    
