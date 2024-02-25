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

"""
    # 초기 바구니 상태
baskets = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    # i번 바구니와 j번 바구니의 공 교환
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
"""

print(*basket)
