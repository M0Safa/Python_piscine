from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:

    lst_operation = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    try:
        return reduce(lst_operation[operation], spells)
    except Exception:
        return -1


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, "fire", 50),
        "ice_enchant": partial(base_enchantment, "ice", 50),
        "lightning_enchant": partial(base_enchantment, "lightning", 50)
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def dispatcher(str: Any) -> str:
        return (f"Spell \"{str}\" is unkown.")

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return (f"Spell did {damage} damage !")

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return (f"You send a {spell} spell !")

    @dispatcher.register(list)
    def _(list: list):
        return (f"Your enregistered {len(list)} spells : {list}.")

    return dispatcher


if __name__ == "__main__":

    print("\nTesting spell reducer...")

    lst_number = [1, 4, 2, 3]

    print(f"Sum: {spell_reducer(lst_number, 'add')}")
    print(f"Product: {spell_reducer(lst_number, 'multiply')}")
    print(f"Max: {spell_reducer(lst_number, 'max')}")
    print(f"Min: {spell_reducer(lst_number, 'min')}")

    print("\nTesting partial enchanter...")

    def enchant(elem: str, power: int, item: str):
        return (f"You give {elem} enchant ({power} power) to your {item}")

    enchant_dict = partial_enchanter(enchant)

    for key, value in enchant_dict.items():
        print(f"{key}: {value('Sword')}")

    print("\nTesting memoized fibonacci...")

    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()
    print(f"dispatcher with an integer: {dispatcher(6)}")
    print(f"dispatcher with an string: {dispatcher('Rage')}")
    print(f"dispatcher with an list: "
          f"{dispatcher(['Fireball', 'Magic missile', 'freeze'])}")
    print("dispatcher with an unknow type: "
          f"{dispatcher({'element': 'Fire'})}")
