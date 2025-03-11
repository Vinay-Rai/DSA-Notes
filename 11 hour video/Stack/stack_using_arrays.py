
class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None]*self.size
        self.top = -1

    def push(self,value):
        if self.top ==self.size:
            return "overflow"
        else:
            self.top+=1
            self.stack[self.top] = value

s = Stack(5)
print(s.stack)
