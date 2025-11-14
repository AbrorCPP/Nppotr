# //Contact manager
import csv

def add_con():
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    with open("contact.csv", "a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, number])

def edit_con():
    with open("contact.csv","r") as f:
        reader = csv.reader(f)
        a = input("For number - 1\nFor name - 2\n--->")
        if a == "1":
            a = input("Enter the name: ")
            for i in reader:
                if i[0].lower() == a.lower():
                    i[1] = input("Enter the number: ")
    with open("contact.csv","w") as f:
        writer = csv.writer(f)
        writer = reader

def delete_con():
    with open("contact.csv","r") as f:
        reader = csv.reader(f)
        for i in reader:
            print(i[0] + i[1])

def prn_con():
    with open("contact.csv","r") as f:
        reader = csv.reader(f)
        ct = 0
        for i in reader:
            if ct != 0:
                print(f"{ct}  {i[0]}  {i[1]}")
            else:
                print(f"\t{i[0]}  {i[1]}")
            ct +=1
def main():
    while True:
        a = int(input("1-Add contact\n2-Edit contact\n3-Delete contact\n4-Print Contact\n5-Exit\n-->"))
        if a == 1:
            add_con()
        elif a == 2:
            edit_con()
        elif a == 3:
            delete_con()
        elif a == 4:
            prn_con()
        else:
            break

main()
