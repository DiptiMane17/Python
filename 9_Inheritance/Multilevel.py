class Grandparent:
    def method(self):
        return "Grandparent"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent"

class Child(Parent):
    def child_method(self):
        return "Child"

child = Child()
print(child.method())       
print(child.parent_method()) 
print(child.child_method())  
