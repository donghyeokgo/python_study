# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())
basket = [0] * N

for p in range (M) :
    i, j, k = map(int, input().split())
    for q in range(i-1, j) :
        basket[q] = k

print(*basket)
