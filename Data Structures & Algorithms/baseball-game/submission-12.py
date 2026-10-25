class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for element in operations:
            if element not in ["+", "D", "C"]:
                stack.append(int(element))
            elif element == "+":
                stack.append(stack[-1] + stack[-2])
            elif element == "D":
                stack.append(stack[-1] * 2)
            elif element == "C":
                stack.pop()
        return sum(stack)