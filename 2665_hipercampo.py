def area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)



N, Xa, Xb = [int(x) for x in input().split(" ")]

P = []
for _ in range(N):
    ponto = tuple(int(x) for x in input().split(" "))
    P.append(ponto)
    
Ps = sorted(P, key = lambda x: x[1], reverse = True)

p1 = (0, Xa)
p2 = (Xb, 0)

graph = {k: [] for k in Ps}

for p3 in range(len(Ps)):    
    for q in Ps[p3+1:]:

        A  = area(p1, p2, Ps[p3]) 

        A1 = area(q, p2, Ps[p3])  
        A2 = area(p1, q, Ps[p3])  
        A3 = area(p1, p2, q)  

        if A == A1 + A2 + A3: 
            graph[Ps[p3]].append(q)

      
dist = {k: 1 for k in Ps}

dist[Ps[0]] = 1

for node in Ps:
    for neighbor in graph[node]:
        if dist[neighbor] < dist[node] + 1:
            dist[neighbor] = dist[node] + 1

print(max(dist.values()))