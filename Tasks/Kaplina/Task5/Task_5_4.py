# 4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, 
# second for count of the upper case letters in the initial string.


def count_low_upper_case(string):
    lowercase_count = 0
    uppercase_count = 0

    for i in string:
        if i.isupper():
            uppercase_count +=1
        if i.islower():
            lowercase_count +=1       
    return lowercase_count, uppercase_count

string = "Barcelona is a city with a wide range of original leisure options that encourage you to visit time and time again. Overlooking the Mediterranean Sea, and famous for Gaudí and other Art Nouveau architecture, Barcelona is one of Europe trendiest cities."
uppercase_count, lowercase_count = count_low_upper_case(string)
print(uppercase_count, lowercase_count)
