
class simpleCalculator:

    #Addition
    @staticmethod
    def add(num1, num2):
        return round(num1 + num2, 6)

    #Subtraction
    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    #Multiplication
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    #Division
    @staticmethod
    def divide(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Divide by Zero is not possible")

    #Sqaure of a number
    @staticmethod
    def square(num1):
        return num1 * num1

    #Squareroot of a number
    @staticmethod
    def squareRoot(num1):
        try:
            return round((num1)**(1/2),8)
        except ValueError:
            print("Invalid Input")





if __name__ == '__main__':

    choice = ""

    

    while choice != "7":
        print("Select the operation:")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Quit")

        choice = input("Enter Choice: ")

        if choice == "1":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(simpleCalculator.add(firstNum, secondNum))

        elif choice == "2":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(simpleCalculator.subtraction(firstNum, secondNum))

        elif choice == "3":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(simpleCalculator.multiply(firstNum, secondNum))

        elif choice == "4":
            firstNum = float(input("Enter first number"))
            secondNum = float(input("Enter Second Number"))
            print(simpleCalculator.divide(firstNum, secondNum))
        elif choice == "5":
            firstNum = float(input("Enter first number"))
            print(simpleCalculator.square(firstNum))
        elif choice == "6":
            firstNum = float(input("Enter first number"))
            print(simpleCalculator.squareRoot(firstNum))
        elif choice == "7":
            break

        else:
            print("Invalid Choice")