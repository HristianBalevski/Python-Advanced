def get_magic_triangle(number_of_rows):
    triangle = [[1], [1, 1]]

    for row in range(2, number_of_rows):
        triangle.append([])
        for col in range(0, len(triangle[-2]) + 1):
            if len(triangle[-1]) == 0 or len(triangle[-2]) == len(triangle[-1]):
                triangle[-1].append(1)
            else:
                triangle[-1].append(triangle[-2][col] + triangle[-2][col - 1])
    return triangle
