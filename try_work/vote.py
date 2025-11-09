age = int(input("Enter your age: "))

if age >= 18:
    print(f"You are {age} years old and you are eligible to vote")
else:
    print(f"You are {age} years old and you are not eligible to vote \n come back in {18-age} years time")
