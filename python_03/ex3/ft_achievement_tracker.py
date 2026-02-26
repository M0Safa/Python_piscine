def display(players, names):
    print("=== Achievement Tracker System ===\n")
    i = 0
    for player in players:
        print(f"Player {names[i]} achievements: {player}")
        i += 1


def all_ach_display(players):
    all_unique = set()
    for player in players:
        all_unique = all_unique.union(player)
    print("All unique achievements:", all_unique)
    print("Total unique achievements:", len(all_unique))
    print("")


def all_common_display(players):
    all_common = players[0]
    for player in players:
        all_common = all_common.intersection(player)
    print("Common to all players:", all_common)


def rarest_display(players):
    i = 0
    rare_ach = set()
    for player in players:
        player_unique = player
        j = 0
        for player_2 in players:
            if i != j:
                player_unique = player_unique.difference(player_2)
            j += 1
        i += 1
        rare_ach = rare_ach.union(player_unique)
    print("Rare achievements (1 player)", rare_ach)


def diff_display(players, names, first, second):
    common = players[first].intersection(players[second])
    first_unique = players[first].difference(common)
    second_unique = players[second].difference(common)
    print(f"{names[first]} vs {names[second]} common:", common)
    print(f"{names[first]} unique:", first_unique)
    print(f"{names[second]} unique:", second_unique)


def main():
    alice_ach = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    charlie_ach = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'}
    bob_ach = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    players = [alice_ach, charlie_ach, bob_ach]
    names = ["alice", "charlie", "bob"]
    display(players, names)
    print("\n=== Achievement Analytics ===")
    all_ach_display(players)
    print("")
    all_common_display(players)
    rarest_display(players)
    print("")
    diff_display(players, names, 0, 2)


main()
