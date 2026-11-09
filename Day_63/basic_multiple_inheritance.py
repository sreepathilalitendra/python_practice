# Day 63: Basic Multiple Inheritance

class Father:

    def father_skills(self):
        print("Father: Gardening")


class Mother:

    def mother_skills(self):
        print("Mother: Cooking")


class Child(Father, Mother):

    def child_skills(self):
        print("Child: Programming")


child1 = Child()

child1.father_skills()
child1.mother_skills()
child1.child_skills()