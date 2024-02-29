l = [3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20]

def get_ranges(l):
    range = []
    start = l[0]

    for i, e in enumerate(l):
        if i > 0 and e != l[i - 1] + 1:
            if start == l[i - 1]:
                range.append(str(start))
            else:
                range.append(f"{start}-{l[i - 1]}")
            start = e

    if start == l[-1]:
        range.append(str(start))
    else:
        range.append(f"{start}-{l[-1]}")

    return ", ".join(range)
print(get_ranges(l))
