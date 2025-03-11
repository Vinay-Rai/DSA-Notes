class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        
    def isempty(self):
        return self.top == None
        
    def push(self,value ):
        new_node= Node(value)
        new_node.next=self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next


    # def pop(self):
    #     # if self.top == None:
    #     if self.isempty():
    #         return "empty stack"
    #     else:
    #         pop_val = self.top.data
    #         self.top = self.top.next
    #         return pop_val
        


de = Stack()
en = Stack()

def queueUsingStacks(op):
    if op =="enqueue":
        data = input("Enter Value")
        en.push(data)
    if op == 'dequeue':

    
