time = input('Enter the time in the format: hh:mm \n')
time = time.split(':')
mm = {
    '1': 'одна(один)',
    '2': 'две(два)',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять',
    '10': 'десять',
    '11': 'одиннадцать',
    '12': 'двенадцать',
    '13': 'тринадцать',
    '14': 'четырнадцать',
    '15': 'пятнадцать',
    '16': 'шестнадцать',
    '17': 'семнадцать',
    '18': 'восемнадцать',
    '19': 'девятнадцать',
    '20': 'двадцать',
    '30': 'тридцать',
    '40': 'сорок'   
    }

hh = {
    '0': 'двенадцатого',
    '1': 'первого',
    '2': 'второго',
    '3': 'третьего',
    '4': 'четвертого',
    '5': 'пятого',
    '6': 'шестого',
    '7': 'седьмого',
    '8': 'восьмого',
    '9': 'девятого',
    '10': 'десятого',
    '11': 'одиннадцатого',
    '12': 'двенадцатого',
}

quarter_h = {
    '1': 'одной',
    '2': 'двух',
    '3': 'трех',
    '4': 'четырех',
    '5': 'пяти',
    '6': 'шести',
    '7': 'семи',
    '8': 'восьми',
    '9': 'девяти',
    '10': 'десяти',
    '11': 'одиннадцати',
    '12': 'двенадцати',
    '13': 'тринадцати',
    '14': 'четырнадцати',
    '15': 'пятнадцати'
    }


if int(time[0]) >= 0 and int(time[0]) < 10:
    time[0] = time[0].replace('0', '', 1).replace(' ', '')
if int(time[1]) > 0 and int(time[1]) < 10:
    time[1] = time[1].replace('0', '', 1).replace(' ', '')

if int(time[0]) > 12 and int(time[0]) < 25:
    time[0] = time[0].replace(time[0], str(int(time[0])-12))


if int(time[1]) > 0 and int(time[1]) < 21 or int(time[1]) == 40:
    print(f'{mm.get(time[1], "invalid number")} минут(а)(ы) {hh.get(time[0],"invalid number")}'),
elif int(time[1]) > 20 and int(time[1]) < 30:
    print(f'{mm["20"]} {mm.get(str(int(time[1])%10), "invalid number")} минут(а)(ы) {hh.get(time[0], "invalid number")}')
elif int(time[1]) == 30:
    print(f'половина {hh[time[0]]}')
elif int(time[1]) > 30 and int(time[1]) < 40:
    print(f'{mm["30"]} {mm.get(str(int(time[1])%10), "invalid number")} минут(а)(ы) {hh.get(time[0], "invalid number")}')
elif int(time[1]) > 40 and int(time[1]) < 45:
    print(f'{mm["40"]} {mm.get(str(int(time[1])%10), "invalid number")} минут(а)(ы) {hh.get(time[0], "invalid number")}')
elif int(time[1]) >= 45:
    print(f'без {quarter_h.get(str(60-int(time[1])), "invalid number")} минут(ы) {mm.get(time[0], "invalid number")}')
elif int(time[1]) == 0 and int(time[0]) < 25:
    if int(time[0]) == 0 and int(time[1]) == 0:
        print("полночь")
    else:
        print(f'{mm.get(time[0], "invalid number")} часа(ов) ровно')
else:
    print("invalid number, please check")







