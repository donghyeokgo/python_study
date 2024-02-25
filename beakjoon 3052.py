numlist = []

for _ in range(10):
    A = int(input())
    numlist.append(A)

result = list(set(X % 42 for X in numlist)) # List Comprehension

print(len(result))



