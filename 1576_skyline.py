from heapq import heappush, heappop


def skyline(predios):
    
    alt_atual     = 0
    skyline       = []
    retira_predio = {}
    heap_predios  = []

    # primeira altura
    heappush(heap_predios, 0)

    for lado, altura in predios:
        if altura < 0:
            heappush(heap_predios, altura)

            if -heap_predios[0] > alt_atual:
                skyline.append([lado, -heap_predios[0]])
                alt_atual = -heap_predios[0]

        else:
            if -altura not in retira_predio:
                retira_predio[-altura] = 0

            retira_predio[-altura] = retira_predio[-altura] + 1

            while (heap_predios[0] in retira_predio) and (retira_predio[heap_predios[0]] > 0):
                retira_predio[heap_predios[0]] = retira_predio[heap_predios[0]] - 1
                heappop(heap_predios)

            if -heap_predios[0] != alt_atual:
                skyline.append([lado, -heap_predios[0]])
                alt_atual = -heap_predios[0]

    return skyline



def nprint(skyline_string):
    n = len(skyline_string)

    for i in range(n - 1):
        print("{} {}".format(skyline_string[i][0], skyline_string[i][1]), end = " ", flush = True)
    
    print("{} 0".format(skyline_string[n-1][0]))
        

predios = []
while True:
    try:
        linha = input()
        
        esqp, altp, dirp = list(map(int, linha.split()))

        predios.append([esqp, -altp])
        predios.append([dirp, altp])

    except EOFError:
        break

predios.sort()

nprint(skyline(predios))