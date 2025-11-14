import csv
import re

x1 = r"^[a-z0-9_-]{3,15}$"
# Username
x2 = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# ?phone number

def add_con():
    a = read_con()
    id1 = len(a)
    while True:
        name = input("Enter the name: ")
        if not re.match(x1, name):
            break
        else:
            print("Invalid name")
    while True:
        phone = input("Enter the phone number: ")
        if re.match(x2, phone):
            break
        else:
            print("Invalid phone number")
    with open('Contacts.csv', "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id1,name,phone])

def read_con():
    with open("Contacts.csv", "r",newline='') as f:
        reader = csv.reader(f)
        s = list(reader)
    return s

def print_con():
    print("/"*50)
    a = read_con()
    for i in a:
        print(f"/{i[0]:<2}: {i[1]:<13} {i[2]}")
    print("/" * 50)

def edit_con():
    x = read_con()
    a = int(input("Enter ID"))
    print("Name: ",x[a][1],"\nPhone Number: ",x[a][2])
    b = int(input("Edit number - 1\nEdit User - 2\n---->"))
    if b == 1:
        b1 = input("Enter new number: ")
        x[a][2] = b1
    elif b == 2:
        b1 = input("Enter new username: ")
        x[a][1] = b1
    with open("Contacts.csv", "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerows(x)

def delete_con():
    x = read_con()
    a = int(input("Enter id : "))
    try:
        x.pop(a)
        print("Done")
    except:
        print("Invalid ID")
    with open("Contacts.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(x)

def id_correct_con():
    x = read_con()
    with open("Contacts.csv", "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(x[0])
        for i in range(1,len(x)):
            x[i][0] = i
            writer.writerow(x[i])

def contacts_e():
    print("__"*40)
    while True:
        id_correct_con()
        a = int(input("|Add contact - 1\n|Edit contact - 2\n|Delete contact - 3\n|Print contacts - 4\n|Exit - 5\n|----->"))
        if a == 1:
            add_con()
        if a == 2:
            edit_con()
        if a == 3:
            delete_con()
        if a == 4:
            print_con()
        else:
            break

def read_sms():
    with open("SMS.csv", "r",newline='') as f:
        reader = csv.reader(f)
        x = list(reader)
    return x

def add_f():
    x = read_con()
    a = []
    for i in x:
        a.append(i[2])
    return a

def send_sms():
    id1 = 0
    name = ""
    phone = ""
    sms = ""
    x = add_f()
    y = read_sms()
    y1 = read_con()
    a = input("Enter the phone number: ")
    if a in x:
        id1 = str(len(y)+1)
        name = y1[x.index(a)][1]
        phone = y1[x.index(a)][2]
        sms = input("Sent text: ")
        with open("SMS.csv", "a",newline='') as f:
            writer = csv.writer(f)
            writer.writerow([id1,name,phone,sms])
    else:
        print("Invalid number")

def delete_sms():
    x = read_sms()
    a = int(input("Enter the text id you want to delete: "))
    t = None
    for i in x:
        if str(a) == i[0]:
            t = x.index(i)
            break
    if t is not None:
        x.pop(t)
        with open("SMS.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(x)
        print("SMS deleted successfully.")
    else:
        print("ID not found.")


def print_sms():
    x = read_sms()
    a = int(input("Print sms by number - 1\nPrint all messages - 2\n---->"))
    if a == 1:
        s = input("Enter the number: ")
        for i in x:
            if i[2] == s:
                print(f"{i[2]} ,{i[3]}")
    elif a == 2:
        print("/"*50)
        for i in x:
            print(f"/{i[0]}:{i[1]} ,  {i[2]},{i[3]}")
        print("/" * 50)
    else:
        pass

def id_correct_sms():
    x = read_sms()
    with open("SMS.csv.csv", "w",newline='') as f:
        writer = csv.writer(f)
        for i in range(len(x)):
            x[i][0] = i
            writer.writerow(x[i])


def sms_e():
    while True:
        id_correct_sms()
        print("="*50)
        a = int(input("|Send sms - 1\n|Delete sms - 2\n|Print sms - 3\n|Exit - 4\n|----->"))
        if a == 1:
            send_sms()
        elif a == 2:
            delete_sms()
        elif a == 3:
            print_sms()
        else:
            break

def main():
    while True:
        print("*"*50)
        a = int(input("|Contacts - 1 \n|SMS - 2\n|Shutdown - 3\n|----->"))
        if a == 1:
            contacts_e()
        elif a == 2:
            sms_e()
        else:
            break

main()
