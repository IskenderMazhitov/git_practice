class Parent:
    def __init__(this, name, age):
        this.name = name
        this.age = age
        this.education = "Bachelor"

    def __str__(this):
        return f"My name is {this.name}, I'm in {this.age}. My education stage is {this.education}"