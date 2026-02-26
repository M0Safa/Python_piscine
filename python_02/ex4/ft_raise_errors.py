def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level}" +
                             " is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}" +
                             " is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}" +
                             " is too low (min 2)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print("Error:", e)


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 4, 5)
    print("\nTesting empty plant name...")
    check_plant_health("", 4, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 11, 4)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 4, 1)
    print("\nAll error raising tests completed!")
