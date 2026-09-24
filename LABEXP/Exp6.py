from dataclasses import dataclass


# Traditional class
class Student:
    def __init__(self, name: str, age: int, mark: float):
        self.name = name
        self.age = age
        self.mark = mark


# Dataclass
@dataclass
class StudentData:
    name: str
    age: int
    mark: float


s1 = Student("Ravi", 20, 85.5)
s2 = StudentData("Ravi", 20, 85.5)

print(s1.name, s1.age, s1.mark)
print(s2)
