
# result = None

try:
    try:
        # print(test)
        inpt = int('0')
        val = 10
        result = val/inpt
        print("the result was calculated:")
        print(result)
    except TypeError:
        print("cannot divide by str value!")
    except ZeroDivisionError as e:
        # print("cannot divide by zero!")
        print(e)
        # print(result)
    # except:
    #     print("something went wrong!")
except NameError as e:
    print("something went wrong!")
    print(e)


try:
    print("everything is correct") 
except:
    print("something went wrong!")
else:
    print("nothing went wrong!")

print("the end")

try:
# raise RuntimeError("BOOM!")
    raise ZeroDivisionError("ANOTHER BOOM!")
except ZeroDivisionError as e:
    print(e)