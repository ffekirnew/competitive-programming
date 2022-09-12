class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        stack = []
        length = len(pushed)
        
        while j < length and i < length: # the condition i < len(pushed) there just so that we don't run into index out of bounds error, because what has not been pushed cannot be popped, so j can never end this loop
            if not stack:
                stack.append(pushed[i])
                i += 1
            
            else:
                if popped[j] == stack[-1]:
                    stack.pop()
                    j += 1
                
                else:
                    stack.append(pushed[i])
                    i += 1
        
        # since if we got out of that loop with out using all in the given arrays, it is probably because of an element failing to be popped in the conditional popped[j] == stack[-1], so we run that test again and return false
        while j < length:
            if popped[j] == stack[-1]:
                    stack.pop()
                    j += 1
            else:
                return False
        
        return True
