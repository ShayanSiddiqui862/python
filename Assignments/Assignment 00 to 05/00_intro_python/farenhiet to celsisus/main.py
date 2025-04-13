def main():
    print("This is farenhiet to celsius converter")
    temp1 = float(input("Enter the temperature in Fahrenheit: "))
    degree_celsius = (temp1 - 32.0) * 5.0 / 9.0
    print(f"Temperature {temp1}F = {degree_celsius:.2f}C")
    
if __name__ == "__main__":
    main()