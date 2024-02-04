# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

# Show the responses to the user in Russian according to the rules listed below:

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)

numbersDictionary = {#Solid numbers
                     1: ["один", "одного", "первого"], 
                     2: ["два", "двух", "второго"],
                     3: ["три", "трех", "третьего"],
                     4: ["четыре", "четырех", "четвертого"],
                     5: ["пять", "пяти", "пятого"],
                     6: ["шесть", "шести", "шестого"],
                     7: ["семь", "семи", "седьмого"],
                     8: ["восемь", "восьми", "восьмого"],
                     9: ["девять", "девяти", "девятого"],
                     10: ["десять", "десяти", "десятого"],
                     11: ["одиннадцать", "одиннадцати", "одиннадцатого"],
                     12: ["двенадцать", "двенадцати"],
                     13: ["тринадцать", "тринадцати"],
                     14: ["четырнадцать", "четырнацати"],
                     15: ["пятнадцать", "пятнадцати"],
                     16: ["шестнадцать", "шестнадцати"],
                     17: ["семнадцать", "семнадцати"],
                     18: ["восемнадцать", "восемнадцати"],
                     19: ["девятнадцать", "девятнадацати"],

                     #Combinations numbers
                     20: ["двадцать", "двадцати"],
                     30: ["тридцать", "тридцати"],
                     40: ["сорок", "сорока"],
                     }

timeDataUnrefined = input("Input your time in hh:mm pattern:")
if(timeDataUnrefined.find(':') == -1):
    print(f"Time isn't in correct pattern")

timeDataList = timeDataUnrefined.split(':')
timeHours = int(timeDataList[0])
timeMinutes = int(timeDataList[1])

if(timeHours > 24 or timeHours < 0 or timeMinutes > 60 or timeMinutes < 0):
    print(f"Time isn't valid, your time is: {timeHours}-{timeMinutes}")

print(f"Your data is {timeHours} hours and {timeMinutes} minutes")

if(timeMinutes == 0):
    print("Do state 1")
elif(timeMinutes < 30):
    print("Do state 2")
elif(timeMinutes == 30):
    print("Do state 3")
elif(timeMinutes > 30 and timeMinutes < 45):
    print("Do state 4")
else:
    print("Do state 5")
