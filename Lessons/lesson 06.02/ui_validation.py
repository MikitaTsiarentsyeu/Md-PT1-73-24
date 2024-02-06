while True:
    time_value = input("enter your time in the hh:mm format:\n")

    if len(time_value) != 5:
        print("incorrect time value length")
        continue

    if time_value.count(':') != 1:
        print("incorrect ':' sign count, there should be only one")
        continue

    if time_value[2] != ':':
        print("':' sign should be in the middle")
        continue

    [hours, minutes] = time_value.split(':')

    if not (hours.isdigit() and minutes.isdigit()):
        print("the hours and minutes values should consist of only digits")
        continue

    
    print(hours, minutes)

    if hours > 23 or minutes > 59:
        print("the time value is wrong")
        continue

    break

print("the main logic starts here")