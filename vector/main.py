def dot_product(vector1, vector2):
    """
    两个向量做点积（结果是一个数）
    :param vector1:
    :param vector2:
    :return:
    """
    if len(vector1) != len(vector2):
        print('向量维度不同，无法进行点积操作')
        return
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def summation_of_vector(vector1, vector2):
    """
    两个向量相加（结果是一个向量）
    :param vector1:
    :param vector2:
    :return:
    """
    if len(vector1) != len(vector2):
        print('向量维度不同，无法进行相加操作')
        return
    return [vector1[i] + vector2[i] for i in range(len(vector1))]


def multiply_vector_with_number(vector, k):
    """
    向量的数乘
    :param vector:
    :param k:
    :return:
    """
    return [vector[i] * k for i in range(len(vector))]


def schmidt(vectors):
    """
    施密特正交化向量组
    :param vectors:
    :return:
    """
    if len(vectors) == 0:
        return []
    results = [vectors[0]]
    for i in range(1, len(vectors)):
        alpha = vectors[i]
        result = alpha
        for j in range(i - 1, -1, -1):
            beta = results[j]
            k = -1 * dot_product(alpha, beta) / dot_product(beta, beta)
            result = summation_of_vector(result, multiply_vector_with_number(beta, k))
        results.append(result)
    return results


if __name__ == '__main__':
    print(schmidt([[1, 1, 1], [1, 2, 3], [1, 4, 9]]))
    print(schmidt([[1, 0, -1, 1], [1, -1, 0, 1], [-1, 1, 1, 0]]))
