
dict_min = {
1:"одна минута",
2:"две минуты",
3:"три минуты",
4:"четыре минуты",
5:"пять минут",
6:"шесть минут",
7:"семь минут",
8:"восемь минут",
9:"девять минут",
10:"десять минут",
11:"одиннадцать минут",
12:"двенадцать минут",
13:"тринадцать минут",
14:"четырнадцать минут",
15:"пятнадцать минут",
16:"шестнадцать минут",
17:"семьнадцать минут",
18:"восемьнадцать минут",
19:"девятнадцать минут",
20:"двадцать минут",
21:"двадцать одна минута",
22:"двадцать две минуты",
23:"двадцать три минуты",
24:"двадцать четыре минуты",
25:"двадцать пять минут",
26:"двадцать шесть минут",
27:"двадцать семь минут",
28:"двадцать восемь минут",
29:"двадцать девять минут",
30:"половина",
31:"тридцать одна минута",
32:"тридцать две минуты",
33:"тридцать три минуты",
34:"тридцать четыре минуты",
35:"тридцать пять минут",
36:"тридцать шесть минут",
37:"тридцать семь минут",
38:"тридцать восемь минут",
39:"тридцать девять минут",
40:"сорок минут",
41:"сорок одна минута",
42:"сорок две минуты",
43:"сорок три минуты",
44:"сорок четыре минуты",
45:"без пятнадцати минут",
46:"без четырнадцати минут",
47:"без тринадцати минут",
48:"без двеннадцати минут",
49:"без одиннадцати минут",
50:"без десяти минут",
51:"без девяти минут",
52:"без восьми минут",
53:"без семи минут",
54:"без шести минут",
55:"без пяти минут",
56:"без четырех минут",
57:"без трех минут",
58:"без двух минут",
59:"без одной минуты"
}

dict_hour = {
1: {
    "exactly": "один час",
    "genitive": "первого",
    "nominative": "час"
},
2:
{
    "exactly": "два часа",
    "genitive": "второго",
    "nominative": "два"
},
3:
{
    "exactly": "три часа",
    "genitive": "третьего",
    "nominative": "три"
},
4:
{
    "exactly": "четыре часа",
    "genitive": "четвертого",
    "nominative": "четыре"
},
5:
{
    "exactly": "пять часов",
    "genitive": "пятого",
    "nominative": "пять"
},
6:
{
    "exactly": "шесть часов",
    "genitive": "шестого",
    "nominative": "шесть"
},
7:
{
    "exactly": "семь часов",
    "genitive": "седьмого",
    "nominative": "семь"
},
8:
{
    "exactly": "восемь часов",
    "genitive": "восьмого",
    "nominative": "восемь"
},
9:
{
    "exactly": "девять часов",
    "genitive": "девятого",
    "nominative": "девять"
},
10:
{
    "exactly": "десять часов",
    "genitive": "десятого",
    "nominative": "десять"
},
11:
{
    "exactly": "одиннадцать часов",
    "genitive": "одиннадцатого",
    "nominative": "одиннадцать"
},
12:
{
    "exactly": "двенадцать часов",
    "genitive": "двенадцатого",
    "nominative": "двенадцать"
},
13:
{
    "exactly": "один час",
    "genitive": "первого",
    "nominative": "час"
},
0:
{
    "exactly": "двенадцать часов",
    "genitive": "двенадцатого",
    "nominative": "двенадцать"
}
}

time = input("Please, enter the time in hh:mm format\n")

if ':' not in time or len(time) != 5:
    print("Please, enter valid time")

else:
  
    time = time.replace(' ', '').strip().split(":")
    hh = int(time[0])
    mm = int(time[1])
    
    if hh > 24 or mm >= 60:
        print("Please, enter valid time")
    elif hh < 0 or mm < 0:
        print("Please, enter valid time")

    else:
        if mm == 00 and hh < 12:
            print(f"{dict_hour[hh]["exactly"]} ровно")
        elif mm == 00 and hh >= 12:
            print(f"{dict_hour[hh-12]["exactly"]} ровно")

        elif mm < 30 and hh < 12:
            print(f"{dict_min[mm]} {dict_hour[hh+1]["genitive"]}")

        elif mm < 30 and hh >= 12:
            print(f"{dict_min[mm]} {dict_hour[hh-11]["genitive"]}")

        elif mm == 30 and hh < 12:
            print(f"половина {dict_hour[hh+1]["genitive"]}")
        elif mm == 30 and hh >= 12:
            print(f"половина {dict_hour[hh-11]["genitive"]}")

        elif mm >= 45 and hh < 12:
            print(f"{dict_min[mm]} {dict_hour[hh+1]["nominative"]}")
        elif mm >= 45 and hh >= 12:
            print(f"{dict_min[mm]} {dict_hour[hh-11]["nominative"]}")

        else:
            if hh < 12:
                print(f"{dict_min[mm]} {dict_hour[hh+1]["genitive"]}")
            else: 
                print(f"{dict_min[mm]} {dict_hour[hh-11]["genitive"]}")


