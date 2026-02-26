def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        print(seed_type.capitalize(), "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed_type.capitalize(), "seeds:", quantity, "grams total")
    elif unit == "area":
        seed_type = seed_type.capitalize()
        print(seed_type, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
