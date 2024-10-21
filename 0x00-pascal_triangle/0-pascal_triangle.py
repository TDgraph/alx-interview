#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n: int):
    """
    Pascal's Triangle

    Args:
        n (int): triangle's deep

    Returns:
        List: Pascal's Triangle List
    """
    pascal_list = []
    if n <= 0:
        return [[]]
    pascal_list.append([1])
    for i in range(1, n):
        tmp = [1]
        for j in range(len(pascal_list[i - 1]) - 1):
            tmp.append(pascal_list[i - 1][j] + pascal_list[i - 1][j + 1])
        tmp.append(1)
        pascal_list.append(tmp)
    return pascal_list

