# Using python 2
# The solution is based on Flood fill
# Greedy solution

import sys
sys.setrecursionlimit(10**9)

n = input()

read_input  = [[[0 for k in xrange(1001)] for j in xrange(21)] for i in xrange(21)]


t_max = 0
for aux in range(n):
	posi1, posi2, posi3 =  [int(k) for k in raw_input().split()]
	read_input[posi1][posi2][posi3] += 1

	t_max = max(t_max, posi3)

position = [[[-1 for k in xrange(1001)] for j in xrange(21)] for i in xrange(21)]

def verify(x, y):
	verified = False
	if x >= 0 and x <= 20:
		if y >= 0 and y <= 20:
			verified = True
	return verified

def solution(x, y, t):
	output = 0
	if verify(x, y):
		if t == t_max:
			position[x][y][t] = read_input[x][y][t]
			return read_input[x][y][t]
		if position[x][y][t] == -1:
				output = max(output, solution(x+1, y, t+1))
				output = max(output, solution(x-1, y, t+1))
				output = max(output, solution(x, y-1, t+1))
				output = max(output, solution(x, y+1, t+1))
				output = max(output, solution(x, y, t+1))
				output += read_input[x][y][t]
				position[x][y][t] = output
		else:
			return position[x][y][t]
	else:
		return 0

	return output
		
print solution(6,6,0)
