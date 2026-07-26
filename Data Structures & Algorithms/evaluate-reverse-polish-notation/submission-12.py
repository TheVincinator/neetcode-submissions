class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for op in tokens:
            if op not in operators:
                stack.append(int(op))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if op == "+":
                    stack.append(num1 + num2)
                elif op == "-":
                    stack.append(num1 - num2)
                elif op == "*":
                    stack.append(num1 * num2)
                else:
                    quotient = num1 / num2
                    stack.append(math.floor(quotient) if quotient > 0 else math.ceil(quotient))
        return stack[0]