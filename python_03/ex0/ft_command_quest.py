import sys


def main():
    print("=== Command Quest ===")
    num = len(sys.argv)
    if num == 1:
        print("No arguments provided!")
    print("Program name:", sys.argv[0])
    i = 1
    if i < num:
        print("Arguments received:", num - i)
    while i < num:
        print(f"Argument {i}:", sys.argv[i])
        i += 1
    print("Total arguments:", num)


main()
