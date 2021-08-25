class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            strs =sorted(strs)
            n = len(min(strs, key = len))
            prefix = ""
            for i in range(n):
                count = 0
                for j in range(1,len(strs)):
                    if strs[j][i] == strs[0][i]:
                        count += 1
                    else:
                        return prefix
                    if count == len(strs)-1:
                        prefix += strs[0][i]
            return prefix
