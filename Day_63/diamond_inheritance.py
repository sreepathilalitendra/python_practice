# Day 63: Diamond Inheritance

class Base:

    def show(self):
        print("Base class")


class Father(Base):

    def show(self):
        print("Father class")
        super().show()


class Mother(Base):

    def show(self):
        print("Mother class")
        super().show()


class Child(Father, Mother):

    def show(self):
        print("Child class")
        super().show()


child1 = Child()

child1.show()

print("\nMRO:")
print([cls.__name__ for cls in Child.mro()])