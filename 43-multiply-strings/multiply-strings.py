class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = mul + result[i + j + 1]
                
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        
        res = ''.join(str(d) for d in result).lstrip('0')
        return res if res else "0"