class MyQueue:


    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack+=[x]
        

    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        return self.stack
        
    def pop(self) -> int:
        if self.stack:
            output = self.stack[0]
            del self.stack[0]
            return output
        return self.stack        
        

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()