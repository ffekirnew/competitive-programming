import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            numbers = [] # this is a stack to keep pure numbers as they come in from the tokens list
            results = [] # this is a stack to keep the result of combined numbers
            stack = [] # this is a stack to keep track of which numbers to combine using the tokens and in which order
            for index in range(len(tokens)):
                token = tokens[index]
                try: # the int(token) will throw an error that will need to be handled, i handle that with the except since that is the only exception to be thrown in the try block, string.isnumeric() was not doing the job for some reason
                    numbers.append(int(token))
                    stack.append("num")
                except:
                    term2 = numbers.pop() if stack.pop() == "num" else results.pop()
                    term1 = numbers.pop() if stack.pop() == "num" else results.pop()
                    
                    result = eval(str(term1) + token + str(term2))
                    result = math.ceil(result) if result < 0 else math.floor(result)
                    results.append(result)
                    stack.append("res")
                    
            return results.pop()