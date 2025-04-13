joke:str = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
sorry:str = "Sorry I only tell jokes"
prompt:str = "What do you want?"
def main():
    user_input = input(prompt)
    user_input = user_input.strip().lower()
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)

if __name__ == "__main__":
    main()