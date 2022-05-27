class Dog:
    def __init__(self):
        print("woof")

    def pee(self):
        print("i will pee")


class Puppy(Dog):
    def __init__(self):
        super().__init__()
        print("im tiny")


p = Puppy()
