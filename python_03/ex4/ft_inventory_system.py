def category_summary(inventory):
    categories = {}
    for item in inventory.values():
        cat = item["category"]
        qty = item["quantity"]
        if cat in categories:
            categories[cat] += qty
        else:
            categories.update({cat: qty})
    return categories


def total_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["quantity"] * item["value"]
    return total


def total_item(inventory):
    total = 0
    for item in inventory.values():
        total += item["quantity"]
    return total


def inventory_disp(player, inventory):
    print(f"=== {player}'s Inventory ===")
    for name, item in inventory.items():
        total = item["quantity"] * item["value"]
        print(f"{name} ({item['category']}, {item['rarity']}): ",
              f"{item['quantity']}x @ {item['value']}",
              f"gold each = {total} gold")
    print(f"Inventory value: {total_value(inventory)} gold")
    print(f"Item count: {total_item(inventory)} items")
    categories = category_summary(inventory)
    print("Categories:", end=" ")
    first = True
    for cat, qty in categories.items():
        if not first:
            print(", ", end="")
        print(f"{cat}({qty})", end="")
        first = False
    print("")


def transfer_item(players, from_inv, to_inv, item_name, quantity):
    print(f"=== Transaction: {from_inv} gives {to_inv} {quantity}",
          f"{item_name} ===")
    if item_name not in players[from_inv]:
        return False
    if players[from_inv][item_name]["quantity"] < quantity:
        return False
    players[from_inv][item_name]["quantity"] -= quantity
    if item_name in players[to_inv]:
        players[to_inv][item_name]["quantity"] += quantity
    else:
        players[to_inv].update({
            item_name: {
                "quantity": quantity,
                "category": players[from_inv][item_name]["category"],
                "rarity": players[from_inv][item_name]["rarity"],
                "value": players[from_inv][item_name]["value"]
            }
        })
    return True


def inv_analytic(players):
    for key in players.keys():
        max_value = key
        max_items = key
        break
    rare_cat = []
    for name, player in players.items():
        if total_value(player) > total_value(players[max_value]):
            max_value = name
        if total_item(player) > total_item(players[max_items]):
            max_items = name
        for name, item in player.items():
            if item["rarity"] == "rare" and name not in rare_cat:
                rare_cat.append(name)
    print("=== Inventory Analytics ===")
    print(f"Most valuable player: {max_value}",
          f"({total_value(players[max_value])} gold)")
    print(f"Most items: {max_items}",
          f"({total_item(players[max_items])} items)")
    print("Rarest items:", end=" ")
    first = True
    for item in rare_cat:
        if not first:
            print(", ", end="")
        print(f"{item}", end="")
        first = False
    print("")


def main():
    players = {
        "alice": {
            "sword": {
                "quantity": 1,
                "category": "weapon",
                "rarity": "rare",
                "value": 500
            },
            "potion": {
                "quantity": 5,
                "category": "consumable",
                "rarity": "common",
                "value": 50
            },
            "shield": {
                "quantity": 1,
                "category": "armor",
                "rarity": "uncommon",
                "value": 200
            }
        },
        "bob": {
            "magic_ring": {
                "quantity": 1,
                "category": "accessory",
                "rarity": "rare",
                "value": 300
                }
                }
        }
    print("=== Player Inventory System ===\n")
    inventory_disp("alice", players["alice"])
    print("")
    flag = transfer_item(players, "alice", "bob", "potion", 2)
    if flag:
        print("Transaction successful!\n")
    else:
        print("Transaction failed!\n")
    print("=== Updated Inventories ===")
    print("Alice potions:", players["alice"]["potion"]["quantity"])
    print("Bob potions:", players["bob"].get("potion", {}).get("quantity", 0))
    print("")
    inv_analytic(players)


main()
