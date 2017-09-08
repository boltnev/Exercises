import unittest


def init_matrix(n, m):
    matrix = [0]*n

    for i in range(n):
        matrix[i] = [0]*m
        for j in range(m):
            matrix[i][j] = i+j+1
    return matrix


def set_to_zero(matrix):
    to_zero_cols = []
    to_zero_rows = []
    # N * M
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i not in to_zero_rows:
                    to_zero_rows.append(i)
                if j not in to_zero_cols:
                    to_zero_cols.append(j)

    # N* M + N
    for row in to_zero_rows:
        matrix[row] = [0] * len(matrix[row])
    # N * M + N + N * M
    for col in to_zero_cols:
        for row in matrix:
            row[col] = 0
    # O(N * M)
    return matrix


def set_to_zero_with_memoizing_in_matrix(matrix):
    first_row_to_zero = False
    first_col_to_zero = False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i == 0:
                    first_row_to_zero = True
                if j == 0:
                    first_col_to_zero = True
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if first_row_to_zero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    if first_col_to_zero:
        for row in matrix:
            row[0] = 0
    return matrix




class SetToZeroesTest(unittest.TestCase):

    def test_set_to_zero_faster(self):
        m = init_matrix(5, 5)
        m[0][0] = 0
        m[3][2] = 0
        set_to_zero(m)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i in (0, 3) or j in(0, 2):
                    self.assertEqual(m[i][j], 0)
                else:
                    self.assertNotEqual(m[i][j], 0)

    def test_set_to_zero_in_place(self):
        m = init_matrix(5, 5)
        m[0][0] = 0
        m[3][2] = 0
        set_to_zero_with_memoizing_in_matrix(m)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i in (0, 3) or j in(0, 2):
                    self.assertEqual(m[i][j], 0)
                else:
                    self.assertNotEqual(m[i][j], 0)


if __name__=="__main__":
    unittest.main()
