class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        for op in range(len(operations)):
            if operations[op] not in ["+", "C","D"]:
                output.append(int(operations[op]))
            elif operations[op] == "+":
                output.append(output[-1] + output[-2])
            elif operations[op] == "D":
                output.append(output[-1] * 2)
            else:
                output.pop()
        return sum(output)


