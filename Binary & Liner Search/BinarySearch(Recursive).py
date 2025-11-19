### Binary search Recursive Method ###

def binary_search(lst, target, left: int, right: int):
    if left > right:
        return None

    mid = (left + right) // 2
    found = lst[mid]

    if found == target:
        return mid

    elif found < target:
        return binary_search(lst=lst, target=target, left=mid + 1, right=right)

    else:
        return binary_search(lst=lst, target=target, left=left, right=mid - 1)

temp = [10, 25, 32, 50, 99, 100, 150, 200, 300, 500, 550, 600, 700]
print(binary_search(temp, 550, 0, 12))