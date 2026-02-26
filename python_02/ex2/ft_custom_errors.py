class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)


def check_plant_health(plant: str, age: int):
    if age > 90:
        raise PlantError(f"The {plant} plant is wilting!")
    else:
        print(f"The {plant} plant is in good health")


def check_water_level(level: int):
    if level < 10:
        raise WaterError("Not enough water in the tank!")
    else:
        print("there is enough water in the tank")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        check_plant_health("tomato", 100)
    except PlantError as e:
        print("Caught PlantError:", e)
    print("")
    try:
        print("Testing WaterError...")
        check_water_level(3)
    except WaterError as e:
        print("Caught WaterError:", e)
    print("")
    print("Testing catching all garden errors...")
    try:
        check_plant_health("tomato", 100)
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        check_water_level(4)
    except GardenError as e:
        print("Caught a garden error:", e)
