def calculate_determinant(matA):
    n = len(matA)
    if n == 1:
        return matA[0][0]
    if n == 2:
        return matA[0][0]*matA[1][1] - matA[0][1]*matA[1][0]
    determinant = 0
    for j in range(n):
        minor_matrix = [row[:j] + row[j+1:] for row in matA[1:]]
        determinant += ((-1)**j) * matA[0][j] * calculate_determinant(minor_matrix)
    return determinant

# Example
matA = [[1, -2, -4],
       [6, -2, 8],
       [3, 2, 1]]
print(calculate_determinant(matA))