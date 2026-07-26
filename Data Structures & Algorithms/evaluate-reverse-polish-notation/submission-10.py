class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for op in tokens:
            if op not in operators:
                stack.append(op)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if op == "+":
                    stack.append(str(num1 + num2))
                elif op == "-":
                    stack.append(str(num1 - num2))
                elif op == "*":
                    stack.append(str(num1 * num2))
                else:
                    quotient = num1 / num2
                    stack.append(str(math.floor(quotient)) if quotient > 0 else str(math.ceil(quotient)))
        print(stack)
        return int(stack[0])