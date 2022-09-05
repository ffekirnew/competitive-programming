class Minmain_stack:

    def __init__(self):
        self.main_stack = [] # a list the perform abstract main_stack actions on
        self.min = None # this will be the minimum number to be returned when getMin() is called
        self.sub_stack = [] # this is a main_stack (a list to be used as a main_stack) to keep track of the substitutions made on the different numbers in the main_stack to get to the current minimum, so when the main_stack is popped, and if that popped item is the minimum, the last substraction made to the number should be reversed by adding by main_stacking from min_sum

    def push(self, val: int) -> None:
        '''
        adds to the stack and if the pushed val is lesser that the current minimum, it sets it to be the new minimum, whilst adding what number was reduced from the previous min to the stack sub_stack
        '''
        if self.main_stack == []:
            self.min = val
            self.sub_stack.append(val)
        elif self.min >= val:
            self.sub_stack.append(self.min - val)
            self.min = val
        self.main_stack.append(val)
        
                
    def pop(self) -> None:
        '''
        pops the main stack and also change the min if it needs to be changed
        '''
        if self.main_stack != []:
            if self.main_stack.pop() == self.min:
                self.min += self.sub_stack.pop()

    def top(self) -> int:
        '''
        returns the last item to be added to the stack, nothing new
        '''
        if self.main_stack != []:
            return self.main_stack[-1]

    def getMin(self) -> int:
        '''
        returns the minimum integer in the stack
        '''
        if self.main_stack != []:
            return self.min


# Your Minmain_stack object will be instantiated and called as such:
# obj = Minmain_stack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()