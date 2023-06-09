class ParentClass:
    def __init__(self):
        self.name = 'parent'
        self.number = 10

    def __str__(self):
        return f'ParentClass name : {self.name}, number : {self.number}'

    def add_num(self, new_number):
        print('부모 : ', new_number, '만큼 더해야지')
        self.number = self.number + new_number

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.name = 'child'

    def add_num(self, new_number):
        print('말 안드러 자식 : ', new_number, '의 두배 만큼 더해야지')
        self.number = self.number + 2 * new_number


parent = ParentClass()
child = ChildClass()
print(parent)
print(child)
print('--------------')

print('add 7 ')
parent.add_num(7)
child.add_num(7)
print(parent)
print(child)