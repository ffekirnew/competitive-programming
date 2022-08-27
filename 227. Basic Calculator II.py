class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s)
        else:
            s = s.replace(" ", "")
            r = [""]
            for i in s:
                if i.isnumeric():
                    r[-1] += i
                else:
                    r.append(i)
                    r.append("")
                    
            s = list(r)
            i = 1
            while i < len(s) - 1:
                if s[i] == '*':
                    s[i - 1] = int(s.pop(i - 1)) * int(s.pop(i))
                elif s[i] == '/':
                    s[i - 1] = int(s.pop(i - 1)) // int(s.pop(i))
                else:
                    i += 2
            j = 1
            while j < len(s) - 1:
                if s[j] == '+':
                    s[j - 1] = int(s.pop(j - 1)) + int(s.pop(j))
                elif s[j] == '-':
                    s[j - 1] = int(s.pop(j - 1)) - int(s.pop(j))
                else:
                    j += 2
            
            return s[0]