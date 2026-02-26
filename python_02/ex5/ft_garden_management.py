class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class NameError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class Plant:
    def __init__(self, name: str, sun: int, water: int):
        self.name = name
        self.sun = sun
        self.water = water


class GardenManager:
    def __init__(self):
        self.__plants = []

    def add_plants(self, plants_lst):
        print("\nAdding plants to garden...")
        try:
            for plant in plants_lst:
                if plant.name == "":
                    raise NameError("Plant name cannot be empty!")
                self.__plants.append(plant)
                print(f"added {plant.name} successfully")
        except NameError as e:
            print("Error adding plant:", e)

    def water_plants(self, water_tank):
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.__plants:
                if water_tank <= 0:
                    raise WaterError("Not enough water in tank")
                water_tank -= 1
                plant.water += 1
                print(f"Watering {plant.name} - sucess")
        except WaterError as e:
            print("Error:", e)
        finally:
            print("Closing watering system (cleanup)")
            return water_tank

    def plants_total(self):
        total = 0
        for plant in self.__plants:
            total += 1
        return total

    def check_plant_health(self):
        print("\nChecking plant health...")
        try:
            for plant in self.__plants:
                name = plant.name
                if plant.water > 10:
                    raise WaterError(f"Water level {plant.water}" +
                                     " is too high (max 10)")
                if plant.water < 1:
                    raise WaterError(f"Water level {plant.water}" +
                                     "is too low (min 1)")
                if plant.sun > 12:
                    raise PlantError(f"Sunlight hours {plant.sun}" +
                                     " is too high (max 12)")
                if plant.sun < 2:
                    raise PlantError(f"Sunlight hours {plant.sun}" +
                                     " is too low (min 2)")
                print(f"{plant.name}: healthy (water: {plant.water}, sun:",
                      f"{plant.sun})")
        except GardenError as e:
            print(f"Error checking {name}:", e)


print("=== Garden Management System ===")
water_tank = 2
plants = [Plant("tomato", 8, 4), Plant("lettuce", 6, 14), Plant("", 5, 6)]
garden = GardenManager()
garden.add_plants(plants)
water_tank = garden.water_plants(water_tank)
garden.check_plant_health()
print("\nTesting error recovery...")
if water_tank < garden.plants_total():
    print("Caught GardenError: Not enough water in tank")
    water_tank += garden.plants_total()
    print("System recovered and continuing...")
print("\nGarden management system test complete!")
