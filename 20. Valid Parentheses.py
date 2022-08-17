class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in s:
                if char in brackets.keys():
                    stack.append(char)
                else:
                    if stack == []:
                        return False
                    temp = stack.pop()
                    if brackets[temp] != char:
                        return False
        return stack == []