# Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

# Show the responses to the user in Russian according to the rules listed below:

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)



user_input = input('Please enter data in the format hh:mm:\n')
print(f'your input: {user_input}')

if len(user_input) != 5:
    print('incorrect input !!!')
    
      
hour = int(user_input.split(':')[0])
minute = int(user_input.split(':')[1])

dict_hour = {
             1: ['один', 'первого'],
             2: ['два', 'второго'],
             3: ['три', 'третьего'],
             4: ['четыре', 'четвертого'],
             5: ['пять', 'пятого'],
             6: ['шесть', 'шестого'],
             7: ['семь', 'седьмого'],
             8: ['восемь', 'восьмого'],
             9: ['девять', 'девятого'],
             10: ['десять', 'десятого'],
             11: ['одиннадцать', 'одинадцатого'],
             12: ['двенадцать', 'двенадцатого'],
             13: ['один', 'первого']
             }

dict_minut = {
             1: ['одна', 'одной'],
             2: ['две', 'двух'],
             3: ['три', 'трех'],
             4: ['четыре', 'четырех'],
             5: ['пять', 'пяти'],
             6: ['шесть', 'шести'],
             7: ['семь', 'семи'],
             8: ['восемь', 'восьми'],
             9: ['девять', 'девяти'],
             10: ['десять', 'десяти'],
             11: ['одиннадцать', 'одиннадцати'],
             12: ['двенадцать', 'двенадцати'],
             13: ['тринадцать', 'тринадцати'],
             14: ['четырнадцать', 'четырнадцати'],
             15: ['пятнадцать', 'пятнадцати'],
             16: ['шестнадцать', 'шестнадцати'],
             17: ['семнадцать', 'семнадцати'],
             18: ['восемнадцать', 'восемнадцати'],
             19: ['девятнадцать', 'девятнадцати'],
             20: 'двадцать',
             30: 'тридцать',
             40: 'сорок',
             50: 'пятьдесят'
             }

if hour == 0:
    hour = 24

if hour >= 13:
    hour -= 12


if minute == 0:
    if hour == 1:
        print(f'{dict_hour.get(hour)[0]} час ровно')
    elif hour == 2 or hour == 3 or hour == 4:
        print(f'{dict_hour.get(hour)[0]} часа ровно')
    else:
        print(f'{dict_hour.get(hour)[0]} часов ровно')


elif minute < 30:
    if minute == 20:
        print(f'{dict_minut.get(minute)} минут {dict_hour.get(hour+1)[1]}')
    elif minute > 20:
        if minute == 21:
            print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минута {dict_hour.get(hour+1)[1]}')
        elif 22 <= minute <= 24:
            print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минуты {dict_hour.get(hour+1)[1]}')        
        else:
            print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минут {dict_hour.get(hour+1)[1]}')
    else:
        if minute == 1 :
            print(f'{dict_minut.get(minute%10)[0]} минута {dict_hour.get(hour+1)[1]}')
        elif 2<=minute<=4 :
            print(f'{dict_minut.get(minute%10)[0]} минуты {dict_hour.get(hour+1)[1]}')        
        else:
            print(f'{dict_minut.get(minute)[0]} минут {dict_hour.get(hour+1)[1]}')
          
                    
elif minute == 30:
    print(f'половина {dict_hour.get(hour+1)[1]}')
    
    
elif 30 < minute < 45 :
    if minute == 31 or minute == 41:
        print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минута {dict_hour.get(hour+1)[1]}')
    elif 32 <= minute <= 34 or 42 <= minute <= 44:
        print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минуты {dict_hour.get(hour+1)[1]}')
    elif minute == 40:
        print(f'{dict_minut.get(minute - minute%10)} минут {dict_hour.get(hour+1)[1]}')      
    else:
        print(f'{dict_minut.get(minute - minute%10)} {dict_minut.get(minute%10)[0]} минут {dict_hour.get(hour+1)[1]}')


elif minute >= 45:
    minute = 60 - minute
    if minute == 1:
        print(f'без {dict_minut.get(minute)[1]} минуты {dict_hour.get(hour+1)[0]}')
    else:
        print(f'без {dict_minut.get(minute)[1]} минут {dict_hour.get(hour+1)[0]}')
        
    



