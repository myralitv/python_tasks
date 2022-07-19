class Student:
    firstName = None
    lastName = None
    group = None
    averageMark = None
    scientificWork = None

    def __init__(self, firstName: str, lastName: str, group: str, scientificWork: int):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.scientificWork = scientificWork

    def if_student(self):
        return self.scientificWork < 1

    def getScholarship(self, marks: tuple):
        if self.if_student():
            self.averageMark = sum(marks) / len(marks)
            if self.averageMark == 5:
                return '100 гривень'
            else:
                return '80 гривень'
        else:
            return f'{self.firstName} {self.lastName} is Aspirant'


class Aspirant(Student):
    def if_aspirant(self):
        return self.scientificWork >= 1

    def getScholarship(self, marks: tuple):
        if self.if_aspirant():
            self.averageMark = sum(marks) / len(marks)
            if self.averageMark == 5:
                return '200 гривень'
            else:
                return '180 гривень'
        else:
            return f'{self.firstName} {self.lastName} isn\'t Aspirant'


if __name__ == '__main__':
    student = Student('Myroslav', 'Lytvynenko', '1', 0)
    print(student.getScholarship((5, 5, 5, 4)))
    aspirant = Aspirant('Nikita', 'Yarmolenko', '2', 1)
    print(aspirant.getScholarship((5, 5, 5, 5)))
