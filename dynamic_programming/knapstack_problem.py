# Recursion Approach
def knapstack(W, wt, val, n):
    if n == 0 or W == 0: return 0
    if wt[n - 1] > W: return knapstack(W, wt, val, n - 1)
    else: return max(val[n - 1] + knapstack(W - wt[n-1], wt, val, n-1), knapstack(W, wt, val, n-1))

# Dynamic Approach
def knapstack1(W, wt, val, n):
    i, w = 0, 0
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[-1][-1]

if __name__ == "__main__":
    val = [60, 10, 100]
    wt = [30, 20, 10]
    W = 50
    print(knapstack(W, wt, val, len(val)))
    print(knapstack1(W, wt, val, len(val)))

