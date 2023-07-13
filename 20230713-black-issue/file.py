class SomeClass:
    type = ""


match (SomeClass.type):
    case _:
        print("Hello there ...")
