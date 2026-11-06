# Practical Dataclass Example

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[int] = field(default_factory=list)

    def calculate_total(self) -> int:
        return sum(self.marks)

    def calculate_average(self) -> float:
        if not self.marks:
            return 0.0

        return self.calculate_total() / len(self.marks)


student1 = Student("Lalitendra", 101, [85, 90, 95])

print("Student:", student1.name)
print("Roll Number:", student1.roll_number)
print("Marks:", student1.marks)
print("Total:", student1.calculate_total())
print("Average:", student1.calculate_average())
