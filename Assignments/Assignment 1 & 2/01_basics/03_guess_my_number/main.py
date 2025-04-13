import random

print("I am thinking of a number between 1 and 99...")
guess =int(input("Take a guess: "))
number:int = random.randint(1,99)
def main():
    guess =int(input("Take a guess: "))
    number:int = random.randint(1,99)
    while guess != number:
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print()
        guess = int(input("Take another guess: "))
    
    print(f"Good job! {number} is the number I was thinking of.")
if __name__ == "__main__":
    main() 