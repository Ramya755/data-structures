matrix = []

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)
