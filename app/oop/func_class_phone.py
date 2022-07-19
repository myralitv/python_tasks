class Phone:
    number = None
    model = None
    weight = None
    name1 = None

    def __init__(self, number: str, model: str, weight: str):
        self.number = number
        self.model = model
        self.weight = weight

    def __str__(self) -> str:
        return f'Phone({self.number}, {self.model}, {self.weight})'

    def getNumber(self):
        return self.number

    def receiveCall(self, name1: str, number1: str = None):
        if number1 is None:
            return f'Телефонує {name1}'
        else:
            return f'Телефонує {name1}, номер телефону {number1}'

    def sendMessage(self, numbers: str):
        return numbers.split(',')


if __name__ == '__main__':
    phone = Phone('14014', 'B12', '612')
    print(phone)
    print(phone.receiveCall('Myroslav', '068674930'))
    print(phone.number)
    print(phone.sendMessage('95003,932992,92349923'))
