class Solution():
    def restoreIpAddresses(self, s):
        def isValid(part):
            len_part = len(part)
            if len_part > 3:
                return False
            if s[0] == '0' and len_part == 1:
                return False
            if int(part) > 255:
                return False
            return True
    
        self.results = []
        def backTracking(s, parts):
            if len(parts) == 3:
                if isValid(s):
                    parts.append(s)
                    self.results.append('.'.join(parts))
                    parts.pop()
                return
            for dot in range(1, min(len(s), 4)):
                part = s[0:dot]
                rest = s[dot:]
                if isValid(part):
                    parts.append(part)
                    backTracking(rest, parts)
                    parts.pop()
        backTracking(s, [])
        return self.results
        
if __name__ == "__main__":
    print(Solution().restoreIpAddresses("12301211"))