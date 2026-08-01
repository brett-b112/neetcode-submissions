class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = [] 
        for op in range(len(operations)):
            if operations[op] not in ["+", "D", "C"]:
                output.append(int(operations[op]))
            else:
                if operations[op] == "+":
                    output.append(output[-1] + output[-2])
                elif operations[op] == "D":
                    output.append(output[-1] * 2)
                elif operations[op] == "C":
                    output.pop()
        return sum(output)


