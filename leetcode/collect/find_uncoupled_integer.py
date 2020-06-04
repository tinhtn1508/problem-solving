if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 4, 3, 1, 2]
    result = 0
    for num in numbers:
        result ^= num
    print(result)