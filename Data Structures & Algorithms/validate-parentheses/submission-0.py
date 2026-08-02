class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        for i in range(len(s)):
            if len(s) == 0:
                return True
            if s[i] in ["(", "{", "["]:
                output.append(s[i])

            elif s[i] in [")", "}", "]"]:
                if len(output) == 0:
                    return False
                elif s[i] == ")" and output[-1] == "(":
                    output.pop()
                elif s[i] == "}" and output[-1] == "{":
                    output.pop()
                elif s[i] == "]" and output[-1] == "[":
                    output.pop()
                else:
                    return False

        if len(output) == 0:
            return True
        else:
            return False 

        