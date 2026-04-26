class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is a mismatch, use it as the new base
                    stack.append(i)
                else:
                    # Valid match found! Calculate length
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len