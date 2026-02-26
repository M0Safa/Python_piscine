def garden_operations(type: str):
    a = 0
    file = "missing.txt"
    try:
        file = "missing.txt"
        if type == "ValueError":
            print("Testing ValueError...")
            a = int("abc")
        elif type == "ZeroDivisionError":
            print("Testing ZeroDivisionError...")
            a = 42 / 0
        elif type == "FileNotFoundError":
            print("Testing FileNotFoundError...")
            a = open(file)
        elif type == "KeyError":
            print("Testing KeyError...")
            plant = {
                "name": "Rose",
                "height": 13
            }
            a = plant["age"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}'")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    if type == "all":
        print("Testing multiple errors together...")
        try:
            a = int("abc")
            a = 42 / 0
            a = open(file)
            plant = {
                "name": "Rose",
                "height": 13
            }
            print(plant["age"])
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            a = "error"
            print(f"Caught an {a}, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("")
    garden_operations("ValueError")
    print("")
    garden_operations("ZeroDivisionError")
    print("")
    garden_operations("FileNotFoundError")
    print("")
    garden_operations("KeyError")
    print("")
    garden_operations("all")
    print("")
    print("All error types tested successfully!")
