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


def row_echelon_of_matrix(matrix):
    """
    求行阶梯形矩阵
    :param matrix:
    :return:
    """
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])

    for r_standard in range(min(rows, cols)):
        c_standard = -1
        for col in range(cols):
            if matrix[r_standard][col] != 0:
                c_standard = col
                break
        if c_standard == -1:
            continue
        for r_compare in range(r_standard + 1, rows):
            if matrix[r_compare][c_standard] == 0:
                continue
            factor = -1. * matrix[r_compare][c_standard] / matrix[r_standard][c_standard]
            matrix[r_compare] = [matrix[r_compare][col] + factor * matrix[r_standard][col] for col in range(cols)]
    return matrix


def simplify_row_echelon_of_matrix(matrix):
    """
    求简化形行阶梯矩阵
    :param matrix:
    :return:
    """
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])

    # 简化形行阶梯矩阵首先是行阶梯矩阵
    matrix = row_echelon_of_matrix(matrix)

    # 非零行的首元素必须是1
    first_elements = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 0:
                first_elements.append((row, col))
                factor = 1. / matrix[row][col]
                matrix[row] = [matrix[row][c] * factor for c in range(cols)]
                break

    # 非零行的首元素所在列的其他元素必须为0
    for row_curr, col in first_elements:
        for row_upper in range(row_curr - 1, -1, -1):
            if matrix[row_upper][col] == 0:
                continue
            factor = -1. * matrix[row_upper][col] / matrix[row_curr][col]
            matrix[row_upper] = [matrix[row_upper][c] + factor * matrix[row_curr][c] for c in range(cols)]

    return matrix


def rank_of_matrix(matrix):
    """
    矩阵的秩
    行阶梯形矩阵的非零行数
    :param matrix:
    :return:
    """
    ans = 0
    for row in row_echelon_of_matrix(matrix):
        is_zero_row = True
        for col in row:
            # 有精度问题，所以使用一个很小的值来判定当前数字是否为0
            if abs(col) > (0.1 ** 10):
                is_zero_row = False
                break
        if not is_zero_row:
            ans += 1
    return ans


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

    # p55/28(1)
    print(reverse_of_matrix([[5, 2, 0, 0], [2, 1, 0, 0], [0, 0, 8, 3], [0, 0, 5, 2]]))

    # p77/1(1-3)
    print(simplify_row_echelon_of_matrix([[1, 0, 2, -1], [2, 0, 3, 1], [3, 0, 4, 3]]))
    print(simplify_row_echelon_of_matrix([[0, 2, -3, 1], [0, 3, -4, 3], [0, 4, -7, -1]]))
    print(simplify_row_echelon_of_matrix([[1, -1, 3, -4, 3], [3, -3, 5, -4, 1], [2, -2, 3, -2, 0], [3, -3, 4, -2, -1]]))

    # p78/10
    print(rank_of_matrix([[3, 1, 0, 2], [1, -1, 2, -1], [1, 3, -4, 4]]))
    print(rank_of_matrix([[3, 2, -1, -3, -1], [2, -1, 3, 1, -3], [7, 0, 5, -1, -8]]))
    print(rank_of_matrix([[2, 1, 8, 3, 7], [2, -3, 0, 7, -5], [3, -2, 5, 8, 0], [1, 0, 3, 2, 0]]))
