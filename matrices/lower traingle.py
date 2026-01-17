n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

total = 0
for i in range(n):
    for j in range(i, n):
        total += matrix[i][j]

print(total)
