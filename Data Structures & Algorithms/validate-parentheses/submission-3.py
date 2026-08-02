class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "]": "[", "}":"{"}
        stack = []

        for character in s:
            if character in matching: # closing bracket
                if not stack or stack[-1] != matching[character]:
                    return False
                stack.pop()
            else:
                stack.append(character)

        if len(stack) == 0:
            return True
        else:
            return False
        #this block is the same as "return not stack"
