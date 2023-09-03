#Phyton program for calculator operator
def calculate(num1, num2, calculator_operator):
    if calculator_operator == '+':
        return num1 + num2
    elif calculator_operator == '-':
        return num1 - num2
    elif calculator_operator == '*':
        return num1 * num2
    elif calculator_operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"

#program to save all input calulcation after each functions is performed
def write_equation_to_file(equation):
    with open('equations.txt', 'a') as file:
        file.write(equation + '\n')

#asking for user input for calculation
def main():
    while True:
        try:
            num1 = int(input("Enter the first number you want to calculate: "))
            num2 = int(input("Enter the second number you want to calculate: "))
            operator = input("Enter the type of calculator operator you want to use (+, -, *, /): ")

            result = calculate(num1, num2, operator)
            equation = f"{num1} {operator} {num2} = {result}"
            print("Result:", result)

            write_equation_to_file(equation)
        except ValueError:
            print("Error: Invalid number entered!")
        except Exception as e:
            print("An error occurred:", str(e))

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            break
if __name__ == '__main__':
    main()

#if user
def calculate(num1, num2, operator_symbol):
    if operator_symbol == '+':
        return num1 + num2
    elif operator_symbol == '-':
        return num1 - num2
    elif operator_symbol == '*':
        return num1 * num2
    elif operator_symbol == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid "

#When equation to txt file..
def write_equation(equation):
    with open("equations.txt", "a") as file:
        file.write(equation + '\n')

#reading equation from txt file 
def read_equations(file_name):
    try:
        with open(file_name, "r") as file:
            equations = file.readlines()
        return [equation.strip() for equation in equations]
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print("An unexpected error occurred:", str(e))
        return None
def main():
    while True:
        option = input("Enter '1' to calculate or '2' to read equations from a txt file: ")

        if option == '1':
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, /): ")

                result = calculate(num1, num2, operator)
                equation = f"{num1} {operator} {num2} = {result}"
                print("Result:", result)

                write_equation(equation)
            except ValueError:
                print("Error: Invalid number entered.")
            except Exception as e:
                print("An unexpected error occurred:", str(e))
        elif option == '2':
            file_name = input("Enter the name of the file: ")
            equations = read_equations(file_name)

            if equations is not None:
                for equation in equations:
                    print(equation)
        else:
            print("Invalid option.")

        choice = input("Do you want to continue (y/n)? ")
        if choice.lower() != 'y':
            break
if __name__ == "__main__":
    main()

