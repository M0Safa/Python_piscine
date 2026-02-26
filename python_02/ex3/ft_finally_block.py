def water_plants(plant_list):
    flag = 1
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant == "None":
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"watering {plant}")
    except Exception as e:
        print("Error:", e)
        flag = 0
    finally:
        print("Closing watering system (cleanup)")
        if flag == 1:
            print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    plant_list1 = ["tomato", "lettuce", "carrots"]
    plant_list2 = ["tomato", "None", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list1)
    print("")
    print("Testing with error...")
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")
