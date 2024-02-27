'1. Write a function that takes two integers as arguments and returns their sum.'
def sums(x, y):
    return x+y
print(sums(2, 3))

'2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.'
def reverse_word(lists):
    list_rev = []
    for word in lists:
        l = word[::-1]
        list_rev.append(l)
    return list_rev
print(reverse_word(['London', 'is', 'the', 'capital', 'of', 'Great', 'Britian']))

'3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.'
def len_word(list_str):
    list_words = []
    for word in list_str:
        if len(word) > 5:
            list_words.append(word)
    return list_words
print(len_word(['London', 'is', 'the', 'capital', 'of', 'Great', 'Britian']))

'4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.'
def count_str(count_n):
    num_lower = 0
    num_upper = 0
    for letter in count_n:
        if letter.islower():
            num_lower +=1
        elif letter.isupper():
            num_upper +=1
    return num_lower, num_upper

print(count_str('London is the capitail of Great Britan'))


'5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:'
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"'

def get_ranges(numbs):

    first = end = numbs[0]

    list_range=[]
    for i in range(1, len(numbs)):
        if numbs[i] - numbs[i-1] == 1:
            end = numbs[i]
        else:
            list_range.append(str(first) if first == end else f'{first}-{end}')
            first = end = numbs[i]
            
    list_range.append(str(first) if first == end else f'{first}-{end}')
    str_range = ', '.join(list_range)
    return str_range


numbs = [1,2,3,4,7,8,10,13,14,15]
print(get_ranges(numbs))