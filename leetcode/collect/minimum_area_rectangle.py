from collections import defaultdict

class Solution():
    def minAreaRect(self, points):
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2])*(y2-y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

if __name__ == "__main__":
    print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
