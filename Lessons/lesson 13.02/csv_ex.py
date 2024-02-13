import csv

with open("data.txt", 'r') as f:
    cars_data = eval(f.read())
    print(type(cars_data))
    print(cars_data)

headlines = ("make", "model", "v", "p", "year", "id")

with open("cars.csv", 'w') as f:
    f.write(','.join(headlines) + "\n")
    for record in cars_data:
        f.write(','.join([str(x) for x in record]) + "\n")

with open("cars.csv", 'r') as f:
    skip = True
    for line in f:
        if skip:
            skip = False
            continue
        print(line.strip().split(','))


with open("cars.csv", 'r') as f:
    reader = csv.DictReader(f, headlines)
    with open("cars_copy.csv", 'w', newline='') as new:
        writer = csv.DictWriter(new, headlines)
        writer.writeheader()
        skip = True
        for record in reader:
            if skip:
                skip = False
                continue
            writer.writerow(record)

