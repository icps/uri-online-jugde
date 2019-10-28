# Using python 2
# Greedy solution

N = int(input())

Quadradonia = [int(e) for e in raw_input().split(' ')]

Noglonia = [int(e) for e in raw_input().split(' ')]

Quadradonia.sort()
Noglonia.sort()

ans = 0

for e in range(N):
	if Noglonia[e] > Quadradonia[ans]:
		ans += 1

print ans
