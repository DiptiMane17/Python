class Parent:
    def method(self):
        print("Parent")

class Child(Parent):
    def child_method(self):
        print("Child")
        
child = Child()
print(child.method())      
print(child.child_method())
