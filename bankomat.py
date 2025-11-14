import json
import re

card_p = { "id":{
    "id" : "1234123412341234",
    "username" : "Tester",
    "code" : 1111,
    "balance": 514000,
    "sms" : "",
}}

x1 = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# Phone num
x3 = r"^[a-z0-9_-]{3,15}$"
# Username
x2 = r"(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)"
# Card id

def create_card(d:dict):
        while True:
            a = int(input("Add card - 1\nExit - 2\n---->"))
            if a == 1:
                while True:
                    id = input("Id = ")
                    if not re.match(x1, id):
                        print("Invalid card id")
                        break
                while True:
                    username = input("Username = ")
                    if not re.match(x3,username):
                        break
                    else:
                        print("Invalid username")
                code = int(input("Code = "))
                balance = int(input("Balance = "))
                cards = { id:{
                    "id" : id,
                    "username": username,
                    "code" : code,
                    "balance" : balance,
                    "sms" : "",
                }}
                with open("cards.json", "r") as f:
                    try:
                        s = json.load(f)
                        s.update(cards)
                    except:
                        s = cards
                with open("cards.json", "w") as f:
                    json.dump(s, f,indent=4)
            else:
                break

def card_balance(d:dict,s1:str):
    with open("cards.json","r") as f:
        a = json.load(f)
    print("-" * 50)
    print("Your current balance is: ",a[s1]["balance"])

def card_extract(d:dict,s1:str):
    with open("cards.json","r") as f:
        s = json.load(f)
        code = s[s1]["code"]
        balance = s[s1]["balance"]
        a = int(input("Enter the sum you want to extract: "))
        if a>s[s1]["balance"]:
            print("Your balance is too low")
        elif a<0:
            print("Invalid format")
        else:
            print("-" * 50)
            print("Your balance was: ",s[s1]["balance"])
            balance = s[s1]["balance"] - a
            print("Extracted balance is: ",a)
            print("Your current balance is: ",balance)
        t = {s1:{
            "id":s1,
            "username":s[s1]["username"],
            "code":code,
            "balance":balance,
            "sms":s[s1]["sms"]
        }}
    with open("cards.json","w") as f:
        s.update(t)
        json.dump(s,f,indent=4)

def card_add(d:dict,s1:str):
    with open("cards.json","r") as f:
        s = json.load(f)
        code = s[s1]["code"]
        balance = s[s1]["balance"]
        a = int(input("Enter the sum you want to add: "))
        if a<0:
            print("Invalid format")
        else:
            print("-"*50)
            print("Your balance was: ", s[s1]["balance"])
            balance = s[s1]["balance"] + a
            print("Additional balance is: ", a)
            print("Your current balance is: ", balance)
        t = {s1: {
            "id": s1,
            "username": s[s1]["username"],
            "code": code,
            "balance": balance,
            "sms": s[s1]["sms"]
        }}
    with open("cards.json","w") as f:
        s.update(t)
        json.dump(s,f,indent=4)

def card_sms_on(d:dict,s1:str):
    with open("cards.json","r") as f:
        s = json.load(f)
        while True:
            a = input("Enter the number to add sms: ")
            if not re.match(x1, a):
                print("Invalid number format. Try again.")
            else:
                print("Your number is:", a)
                sms = a
                break
        t = {s1:{
            "id":s1,
            "username":s[s1]["username"],
            "code":s[s1]["code"],
            "balance":s[s1]["balance"],
            "sms":sms,
        }}
    with open("cards.json","w") as f:
        s.update(t)
        json.dump(s,f,indent=4)

def card_sms_out(d:dict,s1:str):
    with open("cards.json","r") as f:
        s = json.load(f)
        t = {s1: {
            "id": s1,
            "username": s[s1]["username"],
            "code": s[s1]["code"],
            "balance": s[s1]["balance"],
            "sms": "",
        }}
    with open("cards.json","w") as f:
        s.update(t)
        json.dump(s,f,indent=4)

def main(d:dict):
    while True:
        with open("cards.json", "r") as f:
            try:
                s = json.load(f)
            except:
                create_card(d)
            b = input("Include card: ")
            x = b.split()
            b = "".join(x)
            if b == "1":
                create_card(d)
            if b in s:
                t = 1
                while True:
                    b1 = int(input("Enter pin code: "))
                    if b1 == s[b]["code"]:
                        while True:
                            print("_" * 50)
                            a = int(input(
                                "|Balance - 1\n|Extract money - 2\n|Add money - 3\n|Turn sms on - 4\n|Turn sms off - 5\n|Break\n----->"))
                            if a == 1:
                                card_balance(d, b)
                            elif a == 2:
                                card_extract(d, b)
                            elif a == 3:
                                card_add(d, b)
                            elif a == 4:
                                card_sms_on(d, b)
                            elif a == 5:
                                card_sms_out(d, b)
                            else:
                                break
                        break
                    else:
                        t += 1
                    if t > 3:
                        print("Your card is blocked")
                        break
            else:
                print("Invalid format")

main(card_p)
