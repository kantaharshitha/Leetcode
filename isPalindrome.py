class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_val=str(x)
        x_rev=x_val[::-1]
        if x_val!=x_rev:
            return False
        return True           

