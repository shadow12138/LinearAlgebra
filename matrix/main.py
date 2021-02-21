from determinant import main as determinant


def multiplication_by_scalar(matrix, k):
    """
    矩阵的数乘
    :param matrix:
    :param k:
    :return:
    """
    if len(matrix) == 0:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] * k for c in range(cols)] for r in range(rows)]


def summation_of_matrix(m1, m2, symbol=1):
    """
    矩阵加减法（只有同形矩阵才能相加）
    :param m1:
    :param m2:
    :param symbol: 加法为1，减法为-1
    :return:
    """
    r1, r2 = len(m1), len(m2)
    if r1 == r2 == 0:
        return []
    if r1 == 0 or r2 == 0:
        print("非同形矩阵")
        return
    c1, c2 = len(m1[0]), len(m2[0])
    if r1 != r2 or c1 != c2:
        print("非同形矩阵")
        return
    return [[m1[r][c] + (symbol * m2[r][c]) for c in range(c1)] for r in range(r1)]


def subtraction_of_matrix(m1, m2):
    """
    矩阵减法（只有同形矩阵才能相减）
    :param m1:
    :param m2:
    :return:
    """
    return summation_of_matrix(m1, m2, symbol=-1)


def dot_product(array1, array2):
    """
    两个数组的点积
    两个数组可以进行点积的前提是数组长度一致
    :param array1:
    :param array2:
    :return:
    """
    if len(array1) != len(array2):
        print('数组长度不一致，无法进行点积操作')
        return
    return sum([array1[i] * array2[i] for i in range(len(array1))])


def transform_of_matrix(matrix):
    """
    矩阵的转置
    :param matrix:
    :return:
    """
    if len(matrix) == 0:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def multiplication_of_matrix(m_left, m_right):
    """
    矩阵乘法
    矩阵乘法是要分左右的，两个矩阵可以相乘的前提是左边矩阵的列数=右边矩阵的行数
    :param m_left: 左边的矩阵
    :param m_right: 右边的矩阵
    :return:
    """
    r1, r2 = len(m_left), len(m_right)
    if r1 == r2 == 0:
        return []
    if r1 == 0 or r2 == 0:
        print("空矩阵不能与非空矩阵做乘法")
        return
    c1, c2 = len(m_left[0]), len(m_right[0])
    if c1 != r2:
        print("左边矩阵的列数不等于右边矩阵的行数，无法相乘")
        return
    m_right = transform_of_matrix(m_right)
    return [[dot_product(m_left[i], m_right[j]) for j in range(c2)] for i in range(r1)]


def adjoint_of_matrix(matrix):
    """
    求矩阵的伴随矩阵（只有方阵才有伴随矩阵）
    伴随矩阵按行求，按列放
    :param matrix:
    :return:
    """
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])
    if rows != cols:
        print('只有方阵才有伴随矩阵')
        return
    results = []
    for j in range(cols):
        result = []
        for i in range(rows):
            result.append(determinant.algebraic_cofactor_of_determinant(matrix, i, j))
        results.append(result)
    return results


def reverse_of_matrix(matrix):
    """
    求矩阵的逆矩阵（只有方阵才有逆矩阵）
    :param matrix:
    :return:
    """
    if len(matrix) == 0:
        return []
    if len(matrix) != len(matrix[0]):
        print('只有方阵才有逆矩阵')
        return
    val = determinant.calc_determinant(matrix)
    if val == 0:
        print('方阵行列式为0，不存在可逆矩阵')
        return
    adjoint = adjoint_of_matrix(matrix)
    return multiplication_by_scalar(adjoint, 1. / val)


if __name__ == '__main__':
    # p52/1
    print(multiplication_of_matrix([[4, 3, 1], [1, -2, 3], [5, 7, 0]], [[7], [2], [1]]))
    print(multiplication_of_matrix([[1, 2, 3]], [[3], [2], [1]]))
    print(multiplication_of_matrix([[2], [1], [3]], [[-1, 2]]))
    print(multiplication_of_matrix([[2, 1, 4, 0], [1, -1, 3, 4]], [[1, 3, 1], [0, -1, 2], [1, -3, 1], [4, 0, 2]]))

    # p52/2
    a = [[1, 1, 1], [1, 1, -1], [1, -1, 1]]
    b = [[1, 2, 3], [-1, -2, 4], [0, 5, 1]]
    # 计算3AB-2A
    ab3 = multiplication_by_scalar(multiplication_of_matrix(a, b), 3)
    a2 = multiplication_by_scalar(a, 2)
    print(subtraction_of_matrix(ab3, a2))
    # 计算A转置和B的乘积
    print(multiplication_of_matrix(transform_of_matrix(a), b))

    # p52/9(1)(3)
    print(reverse_of_matrix([[1, 2], [2, 5]]))
    print(reverse_of_matrix([[1, 2, -1], [3, 4, -2], [5, -4, 1]]))
