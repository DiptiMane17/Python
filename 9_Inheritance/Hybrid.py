class Parent:
    def method(self):
        return "Parent"

class Child1(Parent):
    def child1_method(self):
        return "Child1 "

class Child2(Parent):
    def child2_method(self):
        return "Child2 "

class GrandChild(Child1, Child2):
    def grandchild_method(self):
        return "Grandchild "

grandchild = GrandChild()
print(grandchild.method())       
print(grandchild.child1_method()) 
print(grandchild.child2_method()) 
print(grandchild.grandchild_method()) 
