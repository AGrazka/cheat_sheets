try:
    x = 2/0
    # x = 2 + 2
except (TypeError, ZeroDivisionError) as err:
    print("not working", err)  # err zwraca treść błędu
else:
    print("working")


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise


class Error(Exception):  # własny wyjątek
    pass


def divide(z, y):
    try:
        result = z / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")  # będzie wykonany bez względu na wynik


try:
    raise KeyboardInterrupt
finally:  # warunek, który musi zostać wykonany bez względu na rezultat try
    print("bye")  # wykonywane przed zakończeniem try
