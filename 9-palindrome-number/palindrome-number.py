class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = str(x)[::-1]

        for i in range(len(x)):
            if x[i] != y[i]:
                return False

        return True