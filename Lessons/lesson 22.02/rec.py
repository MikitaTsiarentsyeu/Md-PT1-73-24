l = [1,2,3,4,5]

def iteration(l, counter=0):
    if counter == len(l):
        return
    iteration(l, counter+1)


l = [3,5,7,65,3,2,12]
target = 2

def search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    
    return -1

l = [1,2,3,4,5,6,7,8,9,10]

def search(l, target, low=0, high=None):

    if high == None:
        high = len(l)-1

    if high < low:
        return -1

    mid = (low + high)//2
    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return search(l, target, low, mid-1)
    else:
        return search(l, target, mid+1, high)
    
print(search(l, 5))