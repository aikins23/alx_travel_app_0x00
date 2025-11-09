import random
secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?"))

match guess:
    case n if n == secret_number: 
        print(f"🎉 Congratulations, the guess number is {secret_number} and you entered {guess} so, you guessed it!")
    case n if n >  secret_number:
        print(f"Oops, your guess number {secret_number} and you entered {guess} so, is a bit high. Try again!")
    case n if n <  secret_number:
        print(f"Nope, your guess number {secret_number} and you entered {guess} so, is a bit low. Give it another shot!")