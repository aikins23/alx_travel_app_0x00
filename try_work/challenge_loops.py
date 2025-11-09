# numbers = [1, 5, 3, 9]
# total = 0
# for number in numbers:
#     total += number
# print(f"the sum of {numbers} ={total}")

import random

secret_number = random.randint(1, 10)
guess_count = 0
guess = 0
while guess != secret_number:
    guess_count += 1
    guess = int(input("Guess a number between 1 and 10: "))
print(f"You guessed {guess_count} times!")