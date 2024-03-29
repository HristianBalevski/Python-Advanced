def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix (mirror it along the main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]
