import sys
from typing import Any, Self


class SomeClass:
    type = ""


def main():
    input = sys.argv[1] if len(sys.argv) > 1 else ""
    match (input + SomeClass.type):
        case "SECRET":
            print("YOU GOT IT")
        case _:
            print("TRY AGAIN")


if __name__ == "__main__":
    main()
