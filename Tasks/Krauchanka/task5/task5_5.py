# 5. Write a function that takes an ordered list of numbers without duplicates and returns 
# a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"




def get_ranges (numbers):
    ranges = []
    number_starting = numbers[0]
    number_final = numbers[0]
    for x in range(1,len(numbers)):
        if numbers[x] == number_final+1:
            number_final = numbers[x]
        else:
            if number_starting == number_final:
                ranges.append(str(number_starting))
            else:
                ranges.append(str(number_starting)+"-"+ str(number_final))
            number_final = numbers[x]
            number_starting = numbers[x]
    if number_starting == number_final:
        ranges.append(str(number_starting))
    else:
        ranges.append(str(number_starting)+"-"+ str(number_final))
    return ", ".join(ranges) 

numbers = [1,2,3,4,5,6,9,10,11,13,14,15,20]
print (get_ranges (numbers))
        

