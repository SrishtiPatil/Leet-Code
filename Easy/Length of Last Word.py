class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for i in reversed(s):
            if i != " ":
                count += 1
            else:
                break
        return count
        
