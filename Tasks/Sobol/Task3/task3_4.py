lst = list(map(int, input("Input values: ").split()))
second_largest = 0
largest = min(lst)
for i in range(len(lst)):
        if lst[i] > largest:
            secondLargest = largest
            largest = lst[i]
        else:
            secondLargest = max(secondLargest, lst[i])
print ("Second largest element is ", secondLargest)            