def check_temperature(temp: str):
    try:
        tmp = int(temp)
        if tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {tmp}°C is perfect for plants!")
    except ValueError:
        print("Error: 'abc' is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    temps = ["25", "abc", "100", "-50"]
    for temp in temps:
        print(f"\nTesting temperature: {temp}")
        check_temperature(temp)
    print("\nAll tests completed - program didn't crash!")
