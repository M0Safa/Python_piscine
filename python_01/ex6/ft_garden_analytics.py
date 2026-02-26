class Plant:
    def __init__(self, name, height, ratio):
        self.name = name
        self.height = height
        self.ratio = ratio
        self.type = "Plant"

    def grow(self):
        print(f"{self.name} grew {self.ratio}cm")
        self.height += self.ratio

    def display(self):
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, ratio, color):
        super().__init__(name, height, ratio)
        self.color = color
        self.type = "Flower"

    def display(self):
        print(f"- {self.name}: {self.height}cm,",
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, ratio, color, prize):
        super().__init__(name, height, ratio, color)
        self.prize = prize
        self.type = "Prize"

    def display(self):
        print(f"- {self.name}: {self.height}cm,",
              f"{self.color} flowers (blooming),",
              f"Prize points: {self.prize}")


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display()


class GardenManger:
    gardens = []

    def __init__(self):
        pass

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    class GardenStats:
        @staticmethod
        def total_plant(garden: Garden) -> int:
            total = 0
            for plant in garden.plants:
                total += 1
            return total

        @staticmethod
        def total_growth(garden: Garden) -> int:
            total = 0
            for plant in garden.plants:
                total += plant.ratio
            return total

        @staticmethod
        def types_count(garden: Garden):
            reg = 0
            flow = 0
            priz = 0
            for plant in garden.plants:
                if plant.type == "Prize":
                    priz += 1
                elif plant.type == "Flower":
                    flow += 1
                else:
                    reg += 1
            print(f"Plant types: {reg} regular, {flow} flowering,",
                  f"{priz} prize flowers")

        @staticmethod
        def get_score(garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.type == "PrizeFlower":
                    score += plant.score
            return score

    def show_stat(self, garden):
        count = self.GardenStats.total_plant(garden)
        growth = self.GardenStats.total_growth(garden)
        print(f"Plants added: {count}, Total growth: {growth}cm")
        self.GardenStats.types_count(garden)

    @classmethod
    def total_gardens(cls) -> int:
        total = 0
        for garden in cls.gardens:
            total += 1
        return total

    @classmethod
    def validate_height(cls):
        for garden in cls.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    print("Height validation test: False")
                    return
        print("Height validation test: True")

    @classmethod
    def gardens_report(cls):
        cls.validate_height
        result = "Garden scores - "
        parts = []
        for garden in cls.gardens:
            score = cls.GardenStats.get_score(garden)
            parts.append(f"{garden.name}: {score}")
        i = 0
        for part in parts:
            if i != 0:
                result += ", "
            result += part
            i += 1
        print(result)
        print(f"Total gardens managed: {cls.total_gardens()}")

    @classmethod
    def create_garden_network(cls):
        alice = Garden("Alice")
        bob = Garden("Bob")
        cls.gardens.append(alice)
        cls.gardens.append(bob)
        return alice, bob


print("=== Garden Management System Demo ===\n")
manager = GardenManger()
alice, bob = GardenManger.create_garden_network()
oak = Plant("Oak Tree", 100, 1)
rose = FloweringPlant("Rose", 25, 2, "red")
sunflower = PrizeFlower("Sunflower", 50, 2, "yellow", 10)
cactus = Plant("Cactus", 28, 1)
alice.add_plant(oak)
alice.add_plant(rose)
bob.add_plant(oak)
bob.add_plant(cactus)
alice.add_plant(sunflower)
print("")
alice.grow_all()
print("")
alice.report()
print("")
manager.show_stat(alice)
print("")
GardenManger.gardens_report()
