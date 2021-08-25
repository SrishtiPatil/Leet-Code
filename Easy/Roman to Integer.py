class Solution:
    def romanToInt(self, s: str) -> int:
        count= 0
        for i in s:
            if i == "I":
                count += 1
            if i == "V":
                count += 5
            if i == "X":
                count += 10
            if i == "L":
                count += 50
            if i == "C":
                count += 100
            if i == "D":
                count += 500
            if i == "M":
                count += 1000
        if s.find('IV') != -1:
            count -= 2
        if s.find('IX') != -1:
            count -= 2
        if s.find('XL') != -1:
            count -= 20
        if s.find('XC') != -1:
            count -= 20
        if s.find('CD') != -1:
            count -= 200
        if s.find('CM') != -1:
            count -= 200
        return count
