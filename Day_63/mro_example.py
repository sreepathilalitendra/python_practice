# Day 63: Method Resolution Order

class Father:

    def show(self):
        print("Father class")


class Mother:

    def show(self):
        print("Mother class")


class Child(Father, Mother):
    pass


child1 = Child()

child1.show()

print("\nMethod Resolution Order:")

for cls in Child.mro():
    print(cls.__name__)

    # Day 63: Cooperative Multiple Inheritance

class Base:

    def show(self):
        print("Base method")


class Father(Base):

    def show(self):
        print("Father method")
        super().show()


class Mother(Base):

    def show(self):
        print("Mother method")
        super().show()


class Child(Father, Mother):

    def show(self):
        print("Child method")
        super().show()


child1 = Child()
child1.show()

print("\nMRO:")
print([cls.__name__ for cls in Child.mro()])