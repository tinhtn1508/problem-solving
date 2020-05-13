import re

class Solution:
    def myAtoi(self, str: str) -> int:
        numregex = re.compile(r'\s*?([-|+]?)([0-9]+)\s*?')
        if numregex.match(str):
            num = 0
            conv = numregex.match(str).group(2)
            sign = numregex.match(str).group(1)
            l = len(conv)
            for c in conv:
                num += (ord(c) - 48)*(10**(l-1))
                l -= 1
            if sign == '-':
                num = -num
                if num < -2**31:
                    return -2**31
                return num
            else:
                if num > 2**31-1:
                    return 2**31-1
                return num
        else:
            return 0

if __name__ == "__main__":
    print(Solution().myAtoi("words and 987"))