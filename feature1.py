class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.education = "Bachelor"

    def __str__(self):
        return f"My name is {self.name}, I'm in {self.age}. My education stage is {self.education}"