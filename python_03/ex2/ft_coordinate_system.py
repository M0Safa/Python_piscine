import sys
import math


def no_input():
    positions = [(31, -36, -24), (44, -15, -10), (-22, -33, 22),
                 (-37, 36, 22), (19, -39, 12), (4, -46, -24),
                 (-39, -23, -11), (14, 27, -24)]
    for pos in positions:
        print("Position created:", pos)
        distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
        print(f"Distance between (0, 0, 0) and {pos}: {distance:.2f}")
        print("")
    print("Unpacking demonstration:")
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    print(f"Coordinates: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


def with_input():
    c = '"'
    flag = False
    for num in sys.argv[1:]:
        try:
            parts = num.split(",")
            if len(parts) != 3:
                print("please enter only 3 int value seperated by ','\n")
            else:
                pos = tuple(int(x) for x in parts)
                print(f"Parsing coordinates: {c}{num}{c}")
                print("Position created:", pos)
                flag = True
                distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
                print(f"Distance between (0, 0, 0) and {pos}: {distance:.1f}")
                print("")
        except ValueError as e:
            print(f"Parsing invalid coordinates: {c}{num}{c}")
            print("Error parsing coordinates:", e)
            error_type = type(e).__name__
            print(f"Error details - Type: {error_type}, Args: {e.args}\n")
    if flag:
        print("Unpacking demonstration:")
        print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
        print(f"Coordinates: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


def main():
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) < 2:
        no_input()
    else:
        with_input()


main()
