while True:

    try:

        Continue = input("Continue? y(es); n(o)")

        if Continue == "y":

            number1 = input("number1:")

            operation = input("operation:")

            number2 = input("number2:")

            number1 = float(number1)

            number2 = float(number2)

            def add(opt1=number1, opt2=number2):

                return (opt1 + opt2)

            def sub(opt1=number1, opt2=number2):

                return (opt1 - opt2)

            def mul(opt1=number1, opt2=number2):

                return (opt1 * opt2)

            def div(opt1=number1, opt2=number2):

                return (opt1 / opt2)

            if operation == "+":

                print(add(opt1=number1, opt2=number2))

            elif operation == "-":

                print(sub(opt1=number1, opt2=number2))

            elif operation == "*":

                print(mul(opt1=number1, opt2=number2))

            elif operation == "/":

                print(div(opt1=number1, opt2=number2))

            else:

                print('Only (+), (-), (*), (/)')

        else:

            print('Program closed')

            break

    except ValueError:

        print("Only numeric values!")
    except ZeroDivisionError:

        print('Cannot divide by 0!')
