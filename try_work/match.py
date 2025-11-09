value = input("Enter a value (number / string): ")
match value:
    case int():
        print(f"You entered {value} and is an integer", value)
    case str():
        print(f"You entered {value} and is a string", value)

        