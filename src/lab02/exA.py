def find_min_max(values):
    if not values:
        raise ValueError("empty list")

    low = values[0]
    high = values[0]
    for num in values:
        if num < low:
            low = num
        if num > high:
            high = num
    return (low, high)


print(find_min_max([3, -1, 5, 5, 0]))  # (-1, 5)
print(find_min_max([42]))  # (42, 42)


def get_unique_sorted(items):
    unique = []
    for item in items:
        found = False
        for u in unique:
            if u == item:
                found = True
        if not found:
            unique.append(item)

    n = len(unique)
    for i in range(n):
        for j in range(n - 1):
            if unique[j] > unique[j + 1]:
                temp = unique[j]
                unique[j] = unique[j + 1]
                unique[j + 1] = temp
    return unique


print(get_unique_sorted([3, 1, 2, 1, 3]))  # [1, 2, 3]
print(get_unique_sorted([]))  # []


def merge_elements(matrix):
    result = []
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("not a list or tuple")
        for element in row:
            result.append(element)
    return result


print(merge_elements([[1, 2], (3, 4, 5)]))  # [1, 2, 3, 4, 5]
