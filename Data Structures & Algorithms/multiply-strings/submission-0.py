class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value1 = 0
        value2 = 0
        for i, digit in enumerate(num1[::-1]):
            value1 += (ord(digit) - ord("0")) * (10 ** i)
        for i, digit in enumerate(num2[::-1]):
            value2 += (ord(digit) - ord("0")) * (10 ** i)
        return str(value1 * value2)