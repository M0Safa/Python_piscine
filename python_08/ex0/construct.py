import sys
import site
import os


def main():
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print("Current Python:", sys.executable)
        print("Virtual Environment:",
              os.path.basename(os.environ["VIRTUAL_ENV"]))
        print("Environment Path:", os.environ["VIRTUAL_ENV"])
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    main()
