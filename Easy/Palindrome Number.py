class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = int("".join(reversed(str(x))))
        if x == y:
            return True
        else:
            return False
