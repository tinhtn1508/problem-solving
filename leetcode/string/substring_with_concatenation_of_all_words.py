from typing import List
import collections

class Solution:
    def findSubString(self, s:str, words: List[str]) -> List[str]:
        if not words: return []
        lw, lws, ls = len(words[0]), len(words), len(s)
        totallen = lw*lws
        if ls < totallen: return []
        rst, ct = [], collections.Counter(words)
        for i in range(ls - totallen + 1):
            ctt, j = {}, 0
            while j < lws:
                curr = s[i + j*lw: i+(j+1)*lw]
                ctt[curr] = ctt.get(curr, 0) + 1
                if ctt[curr] > ct[curr]: break
                j += 1
            if j == lws: rst.append(i)
        return rst

if __name__ == "__main__":
    print(Solution().findSubString("barfoothefoobarman", ["foo", "bar"]))
