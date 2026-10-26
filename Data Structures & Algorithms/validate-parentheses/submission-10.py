class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        stack = []
        valid = {"(": ")", "[": "]", "{":"}"}
        for element in s:
            if element in valid.keys():
                stack.append(element)
            else:
                if len (stack) == 0 or valid[stack[-1]] != element:
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True 
