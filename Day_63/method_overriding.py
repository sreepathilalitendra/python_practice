# Day 63: Method Overriding

class Father:

    def show(self):
        print("This is Father class")


class Mother:

    def display(self):
        print("This is Mother class")


class Child(Father, Mother):

    def show(self):
        print("This is Child class")


child1 = Child()

child1.show()
child1.display()