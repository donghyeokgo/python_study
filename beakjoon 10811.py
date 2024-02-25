# https://www.acmicpc.net/problem/10811

N, M = map(int, input().split())
basket = [x for x in range(1,N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j]) # 인덱싱, reversed

print(*basket)

# GPT solution
'''
    # i부터 j까지의 바구니 순서를 역순으로 변경
    baskets[i-1:j] = baskets[i-1:j][::-1]
'''