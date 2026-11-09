# Day 63: super() with Multiple Inheritance

class Father:

    def show(self):
        print("Father method")
        super().show()


class Mother:

    def show(self):
        print("Mother method")
        super().show()


class Child(Father, Mother):

    def show(self):
        print("Child method")
        super().show()


child1 = Child()

child1.show()