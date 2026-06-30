class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        if digits[len(digits) - 1] != 10:
            return digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 10:
                break
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
        return digits
