class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in valid:
                stack.append(char)
            elif stack and char == valid[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack