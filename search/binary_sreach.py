def binary_search(arr:list, left: int, right: int, x: int) -> int:
    if right >= left:
        mid = left + int((right - left) / 2)
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        return binary_search(arr, mid + 1, right, x)
    return -1

# Execute: python3 binary_sreach.py
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 7
    result = binary_search(arr, 0, len(arr), x)
    print("Index of {}: {}".format(x, result))
