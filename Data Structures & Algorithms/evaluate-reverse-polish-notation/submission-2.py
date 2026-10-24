class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic = set()
        arithmetic.update("+")
        arithmetic.update("-")
        arithmetic.update("*")
        arithmetic.update("/")

        for i in tokens:
            if i not in arithmetic:
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()
                if i == "+":
                    result = first + second
                elif i == "-":
                    result = first - second
                elif i == "*":
                    result = first * second
                else:
                    result = int(first /second)
                stack.append(result)
        return stack[-1]
        