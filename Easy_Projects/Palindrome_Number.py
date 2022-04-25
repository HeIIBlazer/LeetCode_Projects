class Solution:
    def isPalindrome(self, x: int) -> bool:              
        number = x
        Reverse = 0
        while (number>0):
            remainder = x%10
            Reverse = (Reverse*10) + remainder
            number=number//10
        return x == Reverse
        



