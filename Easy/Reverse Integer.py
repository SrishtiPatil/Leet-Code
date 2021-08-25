class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            x = abs(x)
            y = "".join(reversed(str(x)))
            y = int("-"+y)
        else:
            y = int("".join(reversed(str(x))))
        temp = abs(y)
        if temp > 1<<31:
            return 0
        else:
            return y
        
