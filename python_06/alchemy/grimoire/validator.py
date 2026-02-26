def validate_ingredients(ingredients: str) -> str:
    valid_words = {"fire", "water", "earth", "air"}
    for w in valid_words:
        if w in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
