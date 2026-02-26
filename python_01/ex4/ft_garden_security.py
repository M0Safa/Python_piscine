class Secureplant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = 0
        self.age = 0
        self.set_height(height)
        self.set_age(age)
        if (height > 0 and age > 0):
            self.display_update()

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("")
        else:
            self.height = height

    def get_height(self, password: int) -> int:
        if password == 42:
            return self.height
        else:
            print("wrong password")
            return 0

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print("")
        else:
            self.age = age

    def get_age(self, password: int) -> int:
        if password == 42:
            return self.age
        else:
            print("wrong password")
            return 0

    def display_current(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")

    def display_update(self):
        print(f"Plant created: {self.name}")
        print(f"Height updated: {self.height}cm [OK]")
        print(f"Age updated: {self.age} days [OK]")
        print("")


print("=== Garden Security System ===")
plant1 = Secureplant("Rose", -42, 40)
plant2 = Secureplant("Rose", 42, -40)
plant3 = Secureplant("Rose", 20, 40)
print(plant3.get_age(32))
print("")
print(plant3.get_height(42))
print("")
plant3.display_current()
