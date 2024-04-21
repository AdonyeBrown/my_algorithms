def recursive_mat_mult(X, Y):
    # check if matrices can be multiplied
    if len(X[0]) != len(Y):
        return "Invalid matrix dimensions"

    # initialize result matrix with zeros
    res = [[0 for j in range(len(Y[0]))] for i in range(len(X))]

    # recursive multiplication of matrices
    def mult(X, Y, res, i, j, k):
        if i >= len(X):
            return
        if j >= len(Y[0]):
            return mult(X, Y, res, i+1, 0, 0)
        if k >= len(Y):
            return mult(X, Y, res, i, j+1, 0)
        res[i][j] += X[i][k] * Y[k][j]
        mult(X, Y, res, i, j, k+1)

    # perform matrix multiplication
    mult(X, Y, res, 0, 0, 0)
    return res


# example usage
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

result = recursive_mat_mult(A, B)
for row in result:
    print(row)
