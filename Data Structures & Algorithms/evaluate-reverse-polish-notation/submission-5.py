class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack = []
        operators = "+-*/"
        for op in tokens:
            if op not in operators:
                stack.append(int(op))
            else:
                r = stack.pop()
                l = stack.pop()
                if op == "+":
                    stack.append(l + r)
                elif op == "-":
                    stack.append(l - r)
                elif op == "*":
                    stack.append(l * r)
                else:
                    quotient = l / r
                    if quotient < 0:
                        stack.append(math.ceil(quotient))
                    else:
                        stack.append(math.floor(quotient))
        return stack[0]