def main():
    print("This program calculates the perimeter of a triangle")
    print("Please enter the lengths of the three sides of the triangle:")
    num1 = float(input("Enter the first side: "))
    num2 = float(input("Enter the second side: "))
    num3 = float(input("Enter the third side: "))
    print("The perimeter of the triangle is:", str(num1 + num2 + num3))
    
if __name__ == "__main__":
    main()