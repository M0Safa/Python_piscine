def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda x: (base_spell(x) * multiplier)


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(target: str) -> str:
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    def make_a_list(target: str) -> list[str]:
        liste = []
        for spell in spells:
            liste.append(spell(target))
        return liste

    return make_a_list


if __name__ == "__main__":

    print("\nTesting spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    target = "tower"
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined(target)[0]}, "
          f"{combined(target)[1]}.")

    print("\nTesting power amplifier...")

    def magic_missile(power: int) -> int:
        return power

    mega_magic_missile = power_amplifier(magic_missile, 3)
    print(f"Original: {magic_missile(10)}, "
          f"Amplified: {mega_magic_missile(10)}")

    print("\nTesting conditional caster...")

    def ret_condition(target: str) -> bool:
        if target != "immune":
            return True
        return False

    conditional_caste = conditional_caster(ret_condition, fireball)
    print(conditional_caste(target))

    print("\nTesting spell sequence...")

    liste = [fireball, heal, fireball]

    spell_sequenc = spell_sequence(liste)
    print(spell_sequenc(target))
