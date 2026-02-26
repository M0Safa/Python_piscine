class Plant:
    def __init__(self, name, height, age, ratio):
        self.name = name
        self.height = height
        self.ratio = ratio
        self.Age = age

    def grow(self):
        self.height += self.ratio

    def age(self):
        self.Age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.Age} days old")

    def get_grow(self):
        print(f"Growth this week: +{self.ratio * 6}cm")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30, 2)
    plant2 = Plant("Cactus", 15, 120, 1)
    plant3 = Plant("Sunflower", 24, 12, 1.5)
    garden = [plant1, plant2, plant3]
    print("=== Day 1 ===")
    for plant in garden:
        plant.get_info()
        i = 0
        while i < 6:
            plant.age()
            plant.grow()
            i += 1
    print("=== Day 7 ===")
    for plant in garden:
        plant.get_info()
        plant.get_grow()
