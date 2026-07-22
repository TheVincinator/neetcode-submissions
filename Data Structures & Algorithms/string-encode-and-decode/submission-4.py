class Solution:

    def encode(self, strs: List[str]) -> str:
        # 1/H1/e2/l1/o
        # 1/W1/o1/r1/l1/d
        # 1/H1/e2/l1/on1/W1/o1/r1/l1/d

        # 1/H1/32/l1o

        res = ""
        for s in strs:
            for c in s:
                res += "1" + "/" + c
            res += "n"
        return res

    def decode(self, s: str) -> List[str]:
        
        nums = "0123456789"
        i = 0
        res = []
        sub = ""
        while i < len(s):
            j = i
            while s[j] in nums:
                j += 1
            if s[j] == "/":
                sub += int(s[i:j]) * s[j+1]
                i = j + 2
            if s[i] == "n":
                res.append(sub)
                sub = ""
                i += 1
        return res
