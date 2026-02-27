def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '*' + x + '*', spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': sum(powers) / len(powers)
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [{
        'name': " Crystal Orb",
        'power': 85,
        'type': "spell"
    },
                 {
        'name': "Fire Staff",
        'power': 92,
        'type': "spell"
    }
    ]
    sor = artifact_sorter(artifacts)
    print(f"{sor[0]['name']} ({sor[0]['power']}) comes before",
          f"{sor[1]['name']} ({sor[1]['power']})")

    print("\nTesting power filter...")
    strong_artifact = power_filter(artifacts, 90)
    print("artifact with power higher than 90:", strong_artifact[0]['name'])

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    tran = spell_transformer(spells)
    for spell in tran:
        print(spell, end=" ")
    print("\nTesting mage stats...")
    stat = mage_stats(artifacts)
    print(stat)


if __name__ == "__main__":
    main()
