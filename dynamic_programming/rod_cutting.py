# Recursive top-down implementation
def cut_rod(p: list, n: int):
    if n == 0:
        return 0
    q = -1
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q
# Using dynamic programming for optimal rod cutting
def cut_rod_optimal(p: list, n: int):
    r = [0 for _ in range(len(p))]
    def memoized_cut_rod_aux(p, n, r):
        if r[n-1] > 0:
            return r[n-1]
        q = 0
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
        r[n-1] = q
        return q
    return memoized_cut_rod_aux(p, n, r)
# Bottom-up cut rod
def bottom_up_cut_rod(p: list, n: int):
    r = [0 for _ in range(len(p) + 1)]
    for j in range(0, n):
        q = -1
        for i in range(0, j + 1):
            q = max(q, p[i] + r[j-i])
        r[j + 1] = q
    print(r)
    return r[n]

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print("Recursive top-down implementation: {}".format(cut_rod(p, 3)))
    print("Memorized optimal implementation: {}".format(cut_rod_optimal(p, 3)))
    print("Bottom-up implementation: {}".format(bottom_up_cut_rod(p, 3)))