def saco_papai_noel(itens, len_saco, peso_max):
    saco    = [[0 for _ in range(peso_max + 1)] for _ in range(len_saco + 1)]

    for i in range(len_saco + 1):

        for w in range(peso_max + 1):

            if i == 0 or w == 0:
                saco[i][w]    = 0

            elif itens[i - 1][1] <= w:
                saco[i][w] = max(itens[i-1][0] + saco[i-1][w - itens[i-1][1]], saco[i-1][w])

            else:
                saco[i][w]    = saco[i - 1][w]

    return saco


def pacotes_usados(saco, len_saco, peso_max, itens):
    for i in range(len_saco, 0, -1):
        if saco[i][peso_max] != saco[i-1][peso_max]:
            yield itens[i-1][1]
            peso_max -= itens[i-1][1]



N = int(input())

for _ in range(N):
    
    pac     = int(input())
    itens   = [list(map(int, input().split(" "))) for _ in range(pac)]

    saco    = saco_papai_noel(itens, len(itens), 50)

    brinqs  = saco[len(itens)][50]

    valores = list(pacotes_usados(saco, len(itens), 50, itens))

    print('{} brinquedos'.format(brinqs))
    print('Peso: {} kg'.format(sum(valores)))
    print('sobra(m) {} pacote(s)\n'.format(pac - len(valores)))