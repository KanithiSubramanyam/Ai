from sys import maxsize
v=5
def ts_fun(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    while True:
        current_cost=0
        k=s
        for i in range(len(vertex)):
            current_cost+=graph[k][vertex[i]]
            k=vertex[i]
        current_cost+=graph[k][s]
        print(vertex)
        min_path=min(min_path,current_cost)
        if not next_prem(vertex):
            break
    return min_path
def next_prem(vertex):
    n=len(vertex)
    i=n-2
    while i>=0 and vertex[i]> vertex[i+1]:
        i-=1
    if i==-1:
        return False   
    j=i+1
    while j<n and vertex[j]>vertex[i]:
        j+=1
    j-=1
    vertex[i],vertex[j] = vertex[j],vertex[i]
    left=i+1
    right=n-1
    while left<right:
        vertex[left],vertex[right] = vertex[right],vertex[left]
        left+=1
        right-=1
    return True

graph=[[ 0, 10, 15, 20,30], [
     10, 0, 25, 25,15], [15, 25, 0, 30,25], [ 20, 25, 30, 0,15],[25,15,30,35,0]]
s=0
print(ts_fun(graph,s))
