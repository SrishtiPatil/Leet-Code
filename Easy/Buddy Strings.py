class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter
        if len(s) != len(goal) or len(s) == 1:
            return False
        i, j = None, None
        n = len(s)
        for ind in range(n):
            if s[ind] != goal[ind]:
                if i == None:
                    i = ind
                else:
                    j = ind
        if i is None and j is None:
            if n > 2 and len(Counter(s)) < len(s):
                return True
            if len(Counter(s)) == 1:
                return True
            return False
        if i is None or j is None:
            return False
        goal = list(goal)
        goal[i], goal[j] = goal[j], goal[i]
        goal = "".join(goal)
        if goal == s:
            return True
        else:
            return False
