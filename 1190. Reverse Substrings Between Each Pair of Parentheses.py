class Solution:
    def reverseString(self, s: str) -> str:
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i]
        return result
        
    def reverseParentheses(self, s: str) -> str:
        strings = [""]
        index = 0
        for i in s:
            if i == '(':
                strings.append("")
                index += 1
            elif i == ")":
                reversed_s = self.reverseString(strings.pop())
                index -= 1
                strings[index] += reversed_s
            else:
                strings[index] += i
        return strings[0]