'''
Problem:
Write a function:
    def solution(a : list) ->int:
that, given an array A consisting of N integers, returns the maximun sum of
two numbers whose digits add up to an equal sum. If there are no two numbers
whose digits have an equal sum, the function should return -1.
Example:
    A = [51, 71, 17, 42], the function should return 93. There are two pair
    of numbers whose digits add up to an equal sum: (51, 42) and (17, 71).
    The first pair sums up to 93.
'''

def solution(A) -> int:
    def digit_sum(num):
        val = 0
        while num:
            val += num % 10
            num //= 10
        return val
    m = {}
    max_val = -1
    for num in A:
        digit_sum_ = digit_sum(num)
        if digit_sum_ in m:
            other_val = m[digit_sum_]
            max_val = max(max_val, other_val + num)
        else:
            m[digit_sum_] = num
    return max_val

if __name__ == "__main__":
    print(solution([51, 71, 17, 42]))
    print(solution([42, 60, 33, 42]))
    print(solution([51, 32, 43]))