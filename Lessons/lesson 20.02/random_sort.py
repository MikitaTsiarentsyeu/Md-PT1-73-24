import random

def random_sort(l:list):
    count = 0
    while not is_sorted(l):
        swap(l)
        count += 1
    print(count)


def is_sorted(l:list):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
        
    return True

def swap(l:list):
    n = len(l)
    i = generate_index(n)
    j = generate_index(n)
    while i == j:
        j = generate_index(n)
    l[i], l[j] = l[j], l[i]

def generate_index(n:int):
    return random.randint(0, n-1)


l = [1,3,5,7,6,4]
random_sort(l)
print(l)