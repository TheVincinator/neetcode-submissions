class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        i = 0
        j = 0
        maximum = 0
        while j < len(s):
            charCount[s[j]] += 1
            mostFreq = max(charCount.values())
            length = j - i + 1
            if length - mostFreq <= k:
                maximum = max(maximum, length)
            elif length - mostFreq > k:
                while j - i + 1 - max(charCount.values()) > k:
                    charCount[s[i]] -= 1
                    i += 1
            j += 1
        if len(charCount) == 1:
            return charCount[s[0]]
        return maximum
