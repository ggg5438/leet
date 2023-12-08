class Solution:
    def reverse(self, x: int) -> int:
        
        x_abs = abs(x)
        sign = x >= 0
        y_abs = int(str(x_abs)[::-1])
        y = y_abs if sign == True else -y_abs

        if y >2**31 -1 or y< -(2**31):
            return 0
        else:
            return y

        