class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:

            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            else:
                if stack:
                    if stack.pop() != i:
                        return False
                else:
                    return False
        return not stack 