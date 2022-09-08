def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}\n")

def sub(a, b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}\n")

def mul(a, b):
    answer = a * b
    print(f"{str(a)} * {str(b)} = {str(answer)}\n")

def div(a, b):
    answer = a / b
    print(f"{str(a)} / {str(b)} = {str(answer)}\n")


while True:
    print("Addition (A)\nSubtraction (S)\nMultiplication (M)\nDivision (D)\nQuit (Q)\n")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif choice == "S":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice == "M":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == "Q":
        print("Program ended!")
        quit()
    else:
        print("Wrong choice! Please enter a given choice!")
        quit()