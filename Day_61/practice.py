# Day 61: Employee Salary Validation

class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative.")

        self._salary = value


employee1 = Employee("Lalitendra", 25000)

print("Employee:", employee1.name)
print("Original Salary:", employee1.salary)

employee1.salary = 30000

print("Updated Salary:", employee1.salary)