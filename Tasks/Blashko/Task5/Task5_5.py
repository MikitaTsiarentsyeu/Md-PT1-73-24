'''5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"'''



def get_ranges(list_numbers):
    res = []
    res.append(str(list_numbers[0]))
    for i in range(1, len(list_numbers)):
        if list_numbers[i] - list_numbers[i-1] == 1:
            if list_numbers[i] == list_numbers[-1]:
                res[-1] += f"-{str(list_numbers[i])}"
            else:
                continue
        else:
            if res[-1] == str(list_numbers[i-1]):
                res.append(str(list_numbers[i]))
            else:
                res[-1] += f"-{str(list_numbers[i-1])}"
                res.append(str(list_numbers[i]))
            
    res = ', '.join(res)

    return res
            
        

            
            
    
