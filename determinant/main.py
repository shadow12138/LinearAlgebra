from itertools import permutations


def get_reverse_pair_count(array):
    """
    获取一个排列的逆序数
    :param array: 排列
    :return: 逆序数
    """
    ans = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                ans += 1
    return ans


def calc_determinant(determinant):
    """
    计算行列式的值
    :param determinant: 行列式
    :return: 行列式的值
    """
    if len(determinant) == 0:
        return 1
    if len(determinant) != len(determinant[0]):
        print('行列式必须是方阵')
        return

    n = len(determinant)
    ans = 0
    # 行标为标准排列
    rows = [i for i in range(n)]
    # 列标为全排列
    for cols in permutations(rows):
        # 符号为列标逆序对的数量
        curr = 1 if get_reverse_pair_count(cols) % 2 == 0 else -1
        for i in range(n):
            curr *= determinant[rows[i]][cols[i]]
        ans += curr
    return ans


def cofactor_of_determinant(determinant, i, j):
    """
    计算行列式在第i行第j列的余子式
    :param determinant:
    :param i:
    :param j:
    :return:
    """
    if len(determinant) == 0:
        return 1
    rows, cols = len(determinant), len(determinant[0])
    sub_determinant = []
    for r in range(rows):
        if r == i:
            continue
        row = []
        for c in range(cols):
            if c == j:
                continue
            row.append(determinant[r][c])
        sub_determinant.append(row)
    return calc_determinant(sub_determinant)


def algebraic_cofactor_of_determinant(determinant, i, j):
    """
    计算行列式在第i行第j列的代数余子式
    :param determinant:
    :param i:
    :param j:
    :return:
    """
    symbol = 1 if (i + j) % 2 == 0 else -1
    return symbol * cofactor_of_determinant(determinant, i, j)


if __name__ == '__main__':
    # 逆序数相关习题
    # p21/2.(1-4)
    print(get_reverse_pair_count([1, 2, 3, 4]))
    print(get_reverse_pair_count([4, 1, 3, 2]))
    print(get_reverse_pair_count([3, 4, 2, 1]))
    print(get_reverse_pair_count([2, 4, 1, 3]))

    # 行列式相关习题
    # p21/1.(1)、p21/4.(1,2,6)
    print(calc_determinant([[2, 0, 1], [1, -4, -1], [-1, 8, 3]]))
    print(calc_determinant([[4, 1, 2, 4], [1, 2, 0, 2], [10, 5, 2, 0], [0, 1, 1, 7]]))
    print(calc_determinant([[2, 1, 4, 1], [3, -1, 2, 1], [1, 2, 3, 2], [5, 0, 6, 2]]))
    print(calc_determinant([[1, 2, 3, 4], [1, 3, 4, 1], [1, 4, 1, 2], [1, 1, 2, 3]]))
