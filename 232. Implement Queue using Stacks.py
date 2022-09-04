class MyQueue:

    def __init__(self):
        self.__in = [] # the first stack, to be used only for the enequeue operation
        self.__out = [] # the second stack, to be used for the dequeue operation

    def push(self, x: int) -> None:
        '''
        enqueueuing objects to a queue adds the added objects to the back of the data structure, while pushing them to a stack adds them to be the only accessible item in the structure, therefore, if there are any items in the out stack, they should be added to the in first because in my login, the item on the top of the in stack is the last item in the queue structure, so if there are any elements before it, they should be added to the in stack first
        '''
        if self.__out != []:
            for i in range(len(self.__out)):
                self.__in.append(self.__out.pop())
            
        self.__in.append(x)

    def pop(self) -> int:
        '''
        like the push operation, this also contrasts because we are now trying to return the first item added to the queue, meaning the distant item in the in queue, so the stack needs to be reversed and the first item needs to be removed

        i returned the value with out reversing to the in stack because, if the next operation on the queue is dequeue, then the out stack is ready and reversing again won't be required, just poping from the back will work
        '''
        if not self.empty():
            for i in range(len(self.__in)):
                self.__out.append(self.__in.pop())
                
            return self.__out.pop()

    def peek(self) -> int:
        '''
        very similar operations to the pop, just the last wont be removed from the structure
        '''
        if not self.empty():
            for i in range(len(self.__in)):
                self.__out.append(self.__in.pop())
                
            return  self.__out[-1]

    def empty(self) -> bool:
        '''
        evaluates to true if all stacks used are empty
        '''
        return (self.__in == [] and self.__out == [])
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()