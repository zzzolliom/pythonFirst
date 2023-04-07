def get_input_data():
    first_number = input('число')
    sign = input('знак')
    second_number = input('число')
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except:
        print("тут просто калькулятор, надо было вводить число")
        get_input_data()
    try:
        if sign == "=":
            sign = input('Введи другой знак, тут калькулятор')
        elif sign == '+':
            result = first_number + second_number
        elif sign == '-':
            result = first_number - second_number
        elif sign == '*':
            result = first_number * second_number
        elif sign == '/':
            if second_number == 0:
                result = "На 0 делить нелзя, давай заново"
                get_input_data()
            else:
                result = first_number / second_number
        print(result)
        calculator(result)
    except:
        print("Это калькулятор, надо было вводить знак")
        get_input_data()





def calculator(result):
    while True:
        sign = input("Введите знак")
        if sign !="+" and sign !="+" and sign !="+" and sign !="+":
            print("Это калькулятор, тыт производятся элементарные вычисления с числами, соберись")
        else:
            first_number = result
        # print(f"first_number на 34 строке = {first_number}")
            second_number = input("Число")
            try:
                second_number = int(second_number)
            except:
                print("Это калькулятор, тыт производятся элементарные вычисления с числами, соберись")
            try:
                if sign == '+':
                  result = first_number + second_number
                  print(result)
                elif sign == '-':
                    result = first_number - second_number
                    print(result)
                elif sign == '*':
                    result = first_number * second_number
                    print(result)
                elif sign == '/':
                    if second_number == 0:
                        print("На 0 делить нелзя")
                    else:
                        result = first_number / second_number
                    print(result)
                elif sign=="=":
                    print(result)
            except:
                print("Это калькулятор, тыт производятся элементарные вычисления с числами, соберись")



get_input_data()
