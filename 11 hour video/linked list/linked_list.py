class Node:

    def __init__(self,value):
        self.data=value
        self.next=None 

class LinkedList:

    def __init__(self):
        
        #Empty linked list 
        self.head = None
        self.n = 0        #no of nodes

    def __len__(self):       # ye kya hai
        return self.n  

    def insert_head(self,value):
        #check empty linked list
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n= self.n + 1
            return                      #return laga diya taki aage ka code na chale phaltu me
        
        else:
            new_node.next=self.head
            self.head = new_node
            self.n= self.n + 1

    def traverse(self):                       #sab fnction me self dena pada hai kya
        curr = self.head
        
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def __str__(self):               #ye kya hai
        curr = self.head
        result= ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        
        return result[:-2]
    

    def append(self,value):  #insert at tail
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return                            #return laga diya taki aage ka code na chale phaltu me
        
        else:
            curr = self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new_node
            self.n = self.n + 1
    
    def inser_after(self,after,value):

        new_node = Node(value)
        curr=self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr !=None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n +1
        else:
            return 'Item not found'


    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None:
            return "linked list is already empty"
        
        self.head = self.head.next
        self.n=self.n-1


    def pop(self):
        curr = self.head
        #jab ll empty hai
        if self.head== None:
            #empty
            return 'Empty LL'
        curr = self.head
        
        #only one element hai
        if curr.next == None:
            return self.delete_head()     #self.n - 1 kar lena code me
        
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n=self.n-1
        
    def remove(self,value):
        #empty linked list
        if self.head==None:
            return 'empty ll'
        #remove from head node
        if self.head.data==value:
            return self.delete_head()

        curr = self.head
        while curr.next != None:

            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:

            return 'Not found'
        else:
            curr.next = curr.next.next
    

    def search(self,item):

        curr= self.head
        pos = 1

        while curr!=None:
            if curr.data == item:
                return pos
            curr=curr.next
            pos = pos + 1
        
        return 'Not Found'
    
    def __getitem__(self,index):       #to get item using index
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
        
        return "index error"
    

    def replace_max(self,value):

        curr =self.head
        max = self.head.data

        while curr != None:
            if max<curr.data:
                max = curr.data 
            curr = curr.next

        curr =self.head
        while curr != None:
            if curr.data == max:
                curr.data = value
                return
            curr = curr.next
            




 


l = LinkedList()
print(len(l))            #object ki length kaise aa gayi


l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.traverse()
print(l)

l.append(9)
l.append(4)
l.append(5)

l.append(300)


print(l)
# l.clear()
# print(l)
# print("cleared")
# l.remove(9)
print(l)

print(l[8])
l.replace_max(80)
print(l)

