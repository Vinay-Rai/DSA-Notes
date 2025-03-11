class node:
    def __init__(self,value):
        self.data=value
        self.next=None

a=node(1)
b=node(2)
c=node(3)
a.next=b
b.next=c
print(a.next.data)
# print(b)

head = a

# traversing liniked list
while head:
   print(head.data)
   head = head.next

print("the end")

#creating a linked list
class LinkedList:
    def __init__(self):
        
        #Empty linked list
        self.head = None
        self.n=0      #no. of nodes in ll

    def __len__(self):
        return self.n

    def insert_head(self,value):

        new_node = node(value) 

        new_node.next = self.head

        self.head = new_node  

        self.n = self.n + 1
    

L = LinkedList()
print(len(L))
L.insert_head(3)
L.insert_head(4)
L.insert_head( 5)