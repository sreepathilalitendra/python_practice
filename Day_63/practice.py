
# Day 63: Multiple Inheritance and MRO
# Challenge Solutions


# Challenge 1: Basic Inheritance

class Father:

    def father_skill(self):
        print("Father: Gardening")


class Mother:

    def mother_skill(self):
        print("Mother: Cooking")


class Child(Father, Mother):

    def child_skill(self):
        print("Child: Programming")


print("Challenge 1: Basic Inheritance")

child1 = Child()

child1.father_skill()
child1.mother_skill()
child1.child_skill()


# Challenge 2: Multiple Inheritance

class Teacher:

    def teach(self):
        print("Teaching students")


class Researcher:

    def research(self):
        print("Conducting research")


class Professor(Teacher, Researcher):
    pass


print("\nChallenge 2: Multiple Inheritance")

professor1 = Professor()

professor1.teach()
professor1.research()


# Challenge 3: Method Overriding

class Parent1:

    def show(self):
        print("Parent1 method")


class Parent2:

    def display(self):
        print("Parent2 method")


class ChildClass(Parent1, Parent2):

    def show(self):
        print("Child overrides Parent1 method")


print("\nChallenge 3: Method Overriding")

obj = ChildClass()

obj.show()
obj.display()


# Challenge 4: Method Resolution Order

class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print("\nChallenge 4: MRO")

for cls in D.mro():
    print(cls.__name__)


# Challenge 5: Using super()

class Base:

    def show(self):
        print("Base class")


class Parent(Base):

    def show(self):
        print("Parent class")
        super().show()


class ChildWithSuper(Parent):

    def show(self):
        print("Child class")
        super().show()


print("\nChallenge 5: Super Method")

obj = ChildWithSuper()
obj.show()


# Challenge 6: Diamond Inheritance

class A1:

    def display(self):
        print("Class A")


class B1(A1):

    def display(self):
        print("Class B")
        super().display()


class C1(A1):

    def display(self):
        print("Class C")
        super().display()


class D1(B1, C1):

    def display(self):
        print("Class D")
        super().display()


print("\nChallenge 6: Diamond Inheritance")

obj = D1()
obj.display()

print("MRO:", [cls.__name__ for cls in D1.mro()])


# Challenge 7: Employee Management Mini Project

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


class Skills:

    def __init__(self, skills):
        self.skills = skills


class Developer(Employee, Skills):

    def __init__(self, name, age, employee_id, skills):
        Employee.__init__(self, name, age, employee_id)
        Skills.__init__(self, skills)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Skills:", ", ".join(self.skills))


print("\nChallenge 7: Employee Management")

developer1 = Developer(
    "Lalitendra",
    18,
    101,
    ["Python", "Java", "MySQL"]
)

developer1.display()
