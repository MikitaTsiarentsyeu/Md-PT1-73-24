import random
number = []
for i in range(40):
    number.append(random.randint(0, 100))

numumber = sorted(number)

num_set = set(number)
num = list(num_set)


def get_range(numbers):
    ranges = []
    begin = end = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if begin == end:
                ranges.append(str(begin))
            else:
                ranges.append(f'{begin}-{end}')
            begin = end = numbers[i]
    if begin == end:
        ranges.append(str(begin))
    else:
        ranges.append(f'{begin}-{end}')
    return ", ".join(ranges)


print(f"{get_range(num)}.")
