def validate_number(control_value):

    while True:

        x = input(f"Enter your float value higher than {control_value}:")
        try:
            x = float(x)
            if x <= control_value:
                raise RuntimeError("your value is too low, please try again")
        except ValueError:
            print("your value was not a number, please try again")
            continue
        except RuntimeError as e:
            print(e)
            continue
        else:
            break

    return x


def open_file():

    modes = ('w', 'r', 'a')

    while True:

        path = input("enter the path:")
        mode = input("enter the mode (w, r or a):")

        try:
            if mode not in modes:
                raise BrokenPipeError("incorrect mode, please try again")
            
            f = open(path, mode)

        except FileNotFoundError:
            print("file was not found, please try again")
        except BrokenPipeError as e:
            print(e)
            continue
        else:
            break

        return f

print(validate_number(10))

