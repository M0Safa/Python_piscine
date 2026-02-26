import alchemy
import alchemy.elements


def safe_call(func_name) -> None:
    try:
        func = getattr(alchemy, func_name)
        print(f"alchemy.{func_name}():", func())
    except AttributeError:
        print(f"alchemy.{func_name}(): AttributeError - not exposed")


def main():
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())
    print("\nTesting package-level access (controlled by __init__.py):")
    safe_call("create_fire")
    safe_call("create_water")
    safe_call("create_earth")
    safe_call("create_air")
    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


main()
