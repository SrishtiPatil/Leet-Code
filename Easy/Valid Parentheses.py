class Solution:
    def isValid(self, s: str) -> bool:
        pop = ")}]"
        push = "({["
        bracket_dict = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in push:
                stack.append(i)
            elif i in pop:
                if len(stack) == 0:
                    return False
                if stack[-1] == bracket_dict[i]:
                    stack.pop()
                else: return False
        if len(stack) == 0:
            return True
