def transpose(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result


print(transpose([[1, 2, 3]]))       # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))   # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([]))                # []


def row_sums(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    result = []
    for row in mat:
        s = 0
        for x in row:
            s = s + x
        result.append(s)
    return result


print(row_sums([[1, 2, 3], [4, 5, 6]]))    # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))      # [0, 0]
print(row_sums([[0, 0], [0, 0]]))          # [0, 0]


def col_sums(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for j in range(cols):
        s = 0
        for i in range(rows):
            s = s + mat[i][j]
        result.append(s)
    return result


print(col_sums([[1, 2, 3], [4, 5, 6]]))    # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))      # [9, -9]
print(col_sums([[0, 0], [0, 0]]))          # [0, 0]