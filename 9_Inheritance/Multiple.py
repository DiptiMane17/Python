class Parent1:
    def method1(self):
        return "Father"

class Parent2:
    def method2(self):
        return "Mother"

class Child(Parent1, Parent2):
    def child_method(self):
        return "Child"

child = Child()
print(child.method1())      
print(child.method2())      
print(child.child_method())
