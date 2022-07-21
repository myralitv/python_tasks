class Student:
    first_name = None
    last_name = None
    group = None
    average_mark = None

    def __init__(self, first_name: str, last_name: str, group: str, average_mark: int):
        self.firstName = first_name
        self.lastName = last_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return '100 гривень'
        else:
            return '80 гривень'


class Aspirant(Student):
    scientific_work = "Title"

    def __init__(self, first_name: str, last_name: str, group: str, average_mark: int, scientific_work: str):
        Student.__init__(self, first_name, last_name, group, average_mark)
        self.scientific_work = scientific_work

    def set_scientific_work(self):
        return self.scientific_work

    def get_scholarship(self):
        if self.average_mark == 5:
            return '200 гривень'
        else:
            return '180 гривень'


if __name__ == '__main__':
    student = Student('Myroslav', 'Lytvynenko', '1', 4)
    print(student.get_scholarship())
    aspirant = Aspirant('Nikita', 'Yarmolenko', '2', 5, "Number1")
    print(aspirant.get_scholarship())

    object_students_aspirants = []

    object_students_aspirants.append(Student('Myroslav', 'Lytvynenko', '1', 4))
    object_students_aspirants.append(Aspirant('Nikita', 'Yarmolenko', '2', 5, "Number1"))
    object_students_aspirants.append(Student('Vlad', 'Bereka', '2', 5))
    object_students_aspirants.append(Aspirant('Alex', 'Yermolenko', '1', 4, "Number2"))
    object_students_aspirants.append(Student('Dima', 'Kaminskii', '2', 2))
    object_students_aspirants.append(Aspirant('Vova', 'Kondratenko', '1', 3, "Number3"))

    for human in object_students_aspirants:
        print(human.get_scholarship())