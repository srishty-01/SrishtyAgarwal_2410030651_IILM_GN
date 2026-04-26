class Solution:
    def divide(self, dividend, divisor):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = (dividend < 0) != (divisor < 0)
        
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        while a >= b:
            temp_divisor, count = b, 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            a -= temp_divisor
            quotient += count
            
        res = -quotient if negative else quotient
        return max(MIN_INT, min(MAX_INT, res))