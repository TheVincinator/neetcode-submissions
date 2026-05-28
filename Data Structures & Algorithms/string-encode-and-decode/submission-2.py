class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            i += 1
            for j in range(i, i + int(num)):
                word += s[j]
            decoded.append(word)
            i += int(num)
            word = ""
        return decoded