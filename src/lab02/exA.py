def min_max(nums):
    if len(nums) == 0:
        raise ValueError("пустой список")

    minimum = nums[0]
    maximum = nums[0]

    for x in nums:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)

print(min_max([3, -1, 5, 5, 0]))      # (-1, 5)
print(min_max([42]))                   # (42, 42)


def unique_sorted(nums):
    unique = []
    for x in nums:
        found = False
        for u in unique:
            if u == x:
                found = True
        if found == False:
            unique.append(x)

    n = len(unique)
    for i in range(n):
        for j in range(n - 1):
            if unique[j] > unique[j + 1]:
                temp = unique[j]
                unique[j] = unique[j + 1]
                unique[j + 1] = temp
    return unique

print(unique_sorted([3, 1, 2, 1, 3])) # [1, 2, 3]
print(unique_sorted([]))               # []

def flatten(mat):
    result = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("это не список или не кортеж")
        for item in row:
            result.append(item)
    return result


print(flatten([[1, 2], (3, 4, 5)]))   # [1, 2, 3, 4, 5]