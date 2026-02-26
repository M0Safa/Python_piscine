class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def display_info(self):
        print(f"{self.name} (Flower): {self.height}cm,",
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self, area: int):
        print(f"{self.name} provides {area} square meters of shade")

    def display_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,",
              f"{self.diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str,
                 nutration: str):
        super().__init__(name, height, age)
        self.season = season
        self.nutration = nutration

    def ft_nutration(self):
        print(f"{self.name} is rich in {self.nutration}")

    def display_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,",
              f"{self.season} harvest")


print("=== Garden Plant Types ===\n")
rose = Flower("Rose", 33, 20, "red")
rose.display_info()
rose.bloom()
sunflower = Flower("Sunflower", 40, 22, "yellow")
print("")
apple = Tree("Apple tree", 300, 500, 300)
apple.display_info()
apple.produce_shade(78)
lemon = Tree("Lemon tree", 300, 500, 300)
print("")
tomato = Vegetable("Tomato", 9, 2, "summer", "vitamin C")
tomato.display_info()
tomato.ft_nutration()
carrot = Vegetable("Carrot", 14, 3, "spring", "vitamin A")
