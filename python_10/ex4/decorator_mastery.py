import time
from typing import Any


def spell_timer(func: callable) -> callable:

    def calc_time(*args, **kwargs) -> Any:

        print(f"Casting {func.__name__}...")

        begin_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        time_result = end_time - begin_time

        print(f"Spell completed in {time_result:.07f} seconds")

        return result

    return calc_time


def power_validator(min_power: int) -> callable:

    def decorator(func: callable) -> callable:

        def calc_power(*args, **kwargs) -> Any:

            for arg in args:
                if isinstance(arg, int):
                    if arg >= min_power:
                        return func(*args, **kwargs)
                    else:
                        return ("Not enough power to use this spell.")
            return ("Not enough power to use this spell.")

        return calc_power

    return decorator


def retry_spell(max_attempts: int) -> callable:

    def decorator(func: callable) -> callable:

        def try_func(*args, **kwargs) -> Any:

            attempt = 0
            while attempt < max_attempts:

                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempt += 1
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")

            return (f"Spell casting failed after {max_attempts} attempts.")

        return try_func

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and name.replace(" ", "").isalpha())

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power.")


if __name__ == "__main__":

    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting power validator...")

    @power_validator(5)
    def send_spell(power: int, name: str) -> str:
        return (f"You send a {name} spell ({power} power).")

    print(send_spell(6, "Fireball"))
    print(send_spell(3, "Freeze"))

    print("\nTesting retry spell...")

    @retry_spell(5)
    def division_zero(nb: int) -> int:
        return (nb / 0)

    print(send_spell(6, "Fireball"))
    print(division_zero(6))

    print("\nTesting MageGuild...")

    mageguild = MageGuild()

    print(f"{mageguild.validate_mage_name('Veigar')}")
    print(f"{mageguild.validate_mage_name('Blacknight04')}\n")

    print(mageguild.cast_spell('Freeze', 3))
    print(mageguild.cast_spell('Fireball', 16))
