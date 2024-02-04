# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

# Show the responses to the user in Russian according to the rules listed below:

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)

# if Hours time is bigger the 13, change it to (Number - 12) 

numbersDictionary = {#Solid numbers
                     1: ["один", "одной", "первого"], 
                     2: ["два", "двух", "второго"],
                     3: ["три", "трех", "третьего", ],
                     4: ["четыре", "четырех", "четвертого"],
                     5: ["пять", "пяти", "пятого"],
                     6: ["шесть", "шести", "шестого"],
                     7: ["семь", "семи", "седьмого"],
                     8: ["восемь", "восьми", "восьмого"],
                     9: ["девять", "девяти", "девятого"],
                     10: ["десять", "десяти", "десятого"],
                     11: ["одиннадцать", "одиннадцати", "одиннадцатого"],
                     12: ["двенадцать", "двенадцати", "двенадцатого"],
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

minutesAndHoursLabelDictionary = {
    1: ["час", "минута"],
    2: ["часа", "минуты"],
    3: ["часа", "минуты"],
    4: ["часа", "минуты"],
    5: ["часов", "минут"],
    6: ["часов", "минут"],
    7: ["часов", "минут"],
    8: ["часов", "минут"],
    9: ["часов", "минут"],
    10: ["часов", "минут"],
    11: ["часов", "минут"],
    12: ["часов", "минут"],
    13: ["часов", "минут"],
    14: ["часов", "минут"],
    15: ["часов", "минут"],
    16: ["часов", "минут"],
    17: ["часов", "минут"],
    18: ["часов", "минут"],
    19: ["часов", "минут"],

    20: ["", "минут"],
    40: ["", "минут"],
}

timeDataUnrefined = input("Input your time in hh:mm pattern:")
if(timeDataUnrefined.find(':') == -1):
    print(f"Time isn't in correct pattern")

timeDataList = timeDataUnrefined.split(':')
timeHours = int(timeDataList[0])
timeMinutes = int(timeDataList[1])

if(timeHours >= 24 or timeHours < 0 or timeMinutes >= 60 or timeMinutes < 0):
    print(f"Time isn't valid, your time is: {timeHours}-{timeMinutes}")

print(f"Your data is {timeHours} hours and {timeMinutes} minutes")
incrementedHours = timeHours + 1
if(incrementedHours >= 13): 
    incrementedHours -= (incrementedHours // 12) * 12
    if(incrementedHours == 0):
        incrementedHours += 1

if(timeHours >= 13):
    timeHours -= (timeHours // 12) * 12

minutesDecimals = 0
minutesNumbers = 0
if(timeMinutes > 20):
    minutesDecimals = (timeMinutes // 10) * 10
    minutesNumbers = timeMinutes % 10

# main task
if(timeMinutes == 0):
    if(timeHours < 20):
        print(f"[RU] Ваше время: {numbersDictionary[timeHours][0]} {minutesAndHoursLabelDictionary[timeHours][0]} ровно")

elif(timeMinutes < 30):
    timeHoursLabel = numbersDictionary[incrementedHours][2]

    timeMinutesLabel = ""
    if(timeMinutes < 20):
        timeMinutesLabel = f"{numbersDictionary[timeMinutes][0]} {minutesAndHoursLabelDictionary[timeMinutes][1]}"
    else:
        if(minutesNumbers == 0):
            timeMinutesLabel = f"{numbersDictionary[minutesDecimals][0]} {minutesAndHoursLabelDictionary[minutesDecimals][1]}"
        else:
            timeMinutesLabel = f"{numbersDictionary[minutesDecimals][0]} {numbersDictionary[minutesNumbers][0]} {minutesAndHoursLabelDictionary[minutesNumbers][1]}"
        
    print(f"[RU] Ваше время: {timeMinutesLabel} {timeHoursLabel}")

elif(timeMinutes == 30):
    timeHoursLabel = numbersDictionary[incrementedHours][2]
    print(f"[RU] Ваше время: половина {timeHoursLabel}")

elif(timeMinutes > 30 and timeMinutes < 45):
    timeHoursLabel = numbersDictionary[incrementedHours][2]

    timeMinutesLabel = ""
    if(timeMinutes < 20):
        timeMinutesLabel = f"{numbersDictionary[timeMinutes][0]} {minutesAndHoursLabelDictionary[timeMinutes][1]}"
    else:
        if(minutesNumbers == 0):
            timeMinutesLabel = f"{numbersDictionary[minutesDecimals][0]} {minutesAndHoursLabelDictionary[minutesDecimals][1]}"
        else:
            timeMinutesLabel = f"{numbersDictionary[minutesDecimals][0]} {numbersDictionary[minutesNumbers][0]} {minutesAndHoursLabelDictionary[minutesNumbers][1]}"
    
    print(f"[RU] Ваше время: {timeMinutesLabel} {timeHoursLabel}")

else:
    timeHoursLabel = numbersDictionary[incrementedHours][0]
    minutesLabel = ""

    minutesBeforeNextHour = 60 - timeMinutes
    if(minutesBeforeNextHour == 1):
        minutesLabel = "минуты"
    else: 
        minutesLabel = "минут"

    timeMinutesLabel = f"без {numbersDictionary[minutesBeforeNextHour][1]} {minutesLabel}"

    print(f"[RU] Ваше время: {timeMinutesLabel} {timeHoursLabel}")
