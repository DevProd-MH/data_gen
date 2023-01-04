# importing CSV
import csv

# importing random
import random

# getting dataset name
dtnam = input("Enter the name of your dataset : ")

# initializing rows
rows = []
# getting number of columns
lngth = int(input("How many columns do you have? : "))

# initializing header row
header = [" "]

# initializing datatypes of each column
datatype = []

# getting name, datatype, data value for each column
types = []
row = []
num_type = ""
for i in range(lngth):
    print("\n===================================\n - Field N° : " + str(i + 1))
    header.append(input("- Enter Field name : "))
    dttype = input("Enter datatype of this column (Number, String): ")
    if dttype.lower().startswith("n"):
        correct = True
        while correct:
            num_type = input(" * Enter F for Float numbers, I for Integer numbers : ")
            min = input("Enter Min Value : ")
            max = input("Enter Max Value : ")
            if num_type.lower().startswith("f"):
                min = float(min)
                max = float(max)
                correct = False
            elif num_type.lower().startswith("i"):
                min = int(min)
                max = int(max)
                correct = False
            else:
                print("Enter a valid option! ")
            number = [min, max]
            row.append(number)
            types.append("n")
    elif dttype.lower().startswith("s"):
        print(" * Enter your values, leave blank when finished!")
        values = []
        while True:
            val = input("Enter Value : ")
            if val == "":
                break
            values.append(val)

        row.append(values)
        types.append("s")
    else:
        print("Enter a valid option !")

# generating rows
newrow = []
for i in range(int(input("How many lines do you want? : "))):
    newrow = [(i + 1)]
    for j in range(len(types)):
        if types[j] == "n":
            if isinstance(row[j][0], int):
                newrow.append(random.randrange(row[j][0], row[j][1]))
            else:
                newrow.append(random.uniform(row[j][0], row[j][1]))
        elif types[j] == "s":
            newrow.append(random.choice(row[j]))
    rows.append(newrow)

# creating .csv file and writing rows and generated data
with open(dtnam + ".csv", "w") as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(rows)
