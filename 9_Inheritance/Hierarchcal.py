class Parent:
    def method(self):
        return "Parent"

class Child1(Parent):
    def child1_method(self):
        return "Child1"

class Child2(Parent):
    def child2_method(self):
        return "Child2"

child1 = Child1()
child2 = Child2()
print(child1.method())      
print(child1.child1_method()) 
print(child2.method())      
print(child2.child2_method()) 
