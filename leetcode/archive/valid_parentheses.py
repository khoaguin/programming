class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # handle special cases
        if len(s) == 1 or s[0] == ']' or s[0] == ')' or s[0] == '}':
            return False
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            # if find open bracket, add to the stack
            if c in brackets.values():
                stack.append(c)
            # if find close bracket and the corresponding open bracket
            # is in the stack at the last position, remove it from the stack 
            else:
                if brackets[c] in stack:
                    if brackets[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False