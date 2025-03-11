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


    def pop(self):
        # if self.top == None:
        if self.isempty():
            return "empty stack"
        else:
            pop_val = self.top.data
            self.top = self.top.next
            return pop_val
    
    def peek(self):
        # if self.top == None:
        if self.isempty():
            return "Empty stack"
        # print(self.top.data)

        else:
            return  self.top.data
        
    def size(self):
        temp = self.top
        count = 0 
        while temp !=None:
            count+=1
            temp = temp.next
        return count
    
    def reverse(self,text):
        for i in text:
            self.push(i)
        sting = ""
        while not self.isempty():
            sting =sting+str(self.pop())
        print(sting)



def text_Editor(text,pattern):
        u=Stack()
        r=Stack()
        for i in text:
            u.push(i)
        for i in pattern:
            if i == "u":
                a=u.pop()
                r.push(a)
            if i == "r":
                b=r.pop()
                u.push(b)
        res = "" 
        while(not u.isempty()):
            res = u.pop()+res  
        print(res)


l = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]
def celebrity_problem(l):
    s=Stack()
    for i in range(len(l)):
        s.push(i)
    while  s.size() >=2:
        i = s.pop()
        j = s.pop()

        if l[i][j] == 0:
            #j is not a celebrity
            s.push(i)
        else:
            #i is not a celeb
            s.push(j)
    celeb =s.pop()

    for i in range(len(l)):
        if i != celeb:
            if l[i][celeb] ==0 or l[celeb][i] ==1:
                print("No one is celebriy")
                return
    print("the celebrity is ",celeb)



    #balanced paranthesis






                

    






# s = Stack()
# print(s.isempty())
# s.push(4)
# s.push(5)
# s.push(2)
# s.pop()
# s.pop()
# s.pop()
# print(s.pop())
# s.traverse()
# s.peek()
# print()
# print(s.size())

# s.reverse("vinay rai")
            
# text_Editor("raisahab","uuuur")
celebrity_problem(l)
