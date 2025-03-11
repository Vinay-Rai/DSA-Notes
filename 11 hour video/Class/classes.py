#classes are used to implemenation of data structure


# class is a description of an object or bluelprint of object
# it defines various attributes of obeject


class Test:
    x=5   #static variable
    def __init__(self):   #instance method hai
        self.a=3 
        self.b=4
    def show(self):     #min one argument is reuired
        print(self.a,self.b)

    @staticmethod      #no argument is required in method
    def f2():
        print("Hello")

    @classmethod
    def f1(cls):#min one argument is required  in method
        print(cls.x)

#python me new keyword ka use nahi hota object banane ke liye like java cpp


t1=Test()
t2=Test()  #These both are instance object

t1.show()  #yahan par t1 object show me pass ho jayega implicitly

#calling class method 
Test.f1()


Test.f2()  #calling static method using class name and object name
t1.f2()

#pyhton does not have acces specifiers