class Sample:
    class_attribute = "Class Attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def instance_method(self):
        return f"Instance method called. Instance attribute: {self.instance_attribute}"

    @classmethod
    def class_method(cls):
        return f"Class method called. Class attribute: {cls.class_attribute}"

    @staticmethod
    def static_method(param):
        return f"Static method called with parameter: {param}"

sample = Sample("Instance Attribute")

print(sample.instance_method())

print(Sample.class_method())

print(Sample.static_method("Parameter"))
