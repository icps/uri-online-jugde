def festa(graph, vertice, X, visitado, anims):
    
    if visitado[vertice - 1] == True:
        return anims[vertice - 1]
        
    visitado[vertice - 1] = True
    
    if len(graph[vertice]) == 0:
        anims[vertice - 1] = X[vertice - 1]
        return X[vertice - 1]
    
    sum1 = X[vertice - 1]
    for filhos in graph[vertice]:
        for neto in graph[filhos]:
            if visitado[neto - 1] == True:
                sum1 = sum1 + anims[neto - 1]
                
            else:
                sum1 = sum1 + festa(graph, neto, X, visitado, anims)
                
    sum2 = 0
    for filho in graph[vertice]:
        if visitado[filho - 1] == True:
            sum2 = sum2 + anims[filho - 1]
        else:
            sum2 = sum2 + festa(graph, filho, X, visitado, anims)
            
    if sum1 > sum2:
        anims[vertice - 1] = sum1
    else:
        anims[vertice - 1] = sum2

    return max(sum1, sum2)
    

N = input()
X = [int(x) for x in input().split(" ")]
P = [int(p) for p in input().split(" ")]


graph = {k: [] for k in range(1, len(X) + 1)}

for enum, boss in enumerate(P):
    graph[boss].append(enum + 2)


visitado = [False] * len(graph)

anims = X
valor = festa(graph, 1, X, visitado, anims)
print(valor)