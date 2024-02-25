# https://www.acmicpc.net/problem/10813

N, M = map(int, input().split())

basket = [0] * N

for i in range(N):
    basket[i] = i+1

tmp = [0]

for p in range(M) :
    i,j = map(int, input().split())
    tmp[0] = basket[i-1] 
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp[0]
    # print(basket)

print(*basket)
