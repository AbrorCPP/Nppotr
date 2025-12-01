class User:
    def __init__(self, username, phone, seria, age, password):
        self.username  = username
        self.phone     = phone
        self.seria     = seria
        self.age       = age
        self.password  = password
        self.is_active = True
        self.is_admin  = False


class Car:
    def __init__(self, model, brand, year, seria ):
        self.model  = model
        self.brand  = brand
        self.year   = year
        self.seria  = seria
        self.is_active = True

class Order:
    def __init__(self,user_id,car_id,date_start,date_end):
        self.user_id    = user_id
        self.car_id     = car_id
        self.date_start = date_start
        self.date_end   = date_end
        self.is_active  = True

class Massage:
    def __init__(self,user_id,car_id):
        self.user_id = user_id
        self.car_id = car_id
        self.Let = False

class Park:
    def __init__(self,title):
        self.title   =title
        self.users   =[]
        self.cars    =[]
        self.orders  =[]
        self.massages = []

    def show_massages(self):
        i =0
        for ms in self.massages:
            i+=1
            print(f"{i}. {self.users[ms.user_id].username} wants to take {self.cars[ms.car_id].title}.")
        a = int(input("Select one: "))
        i = 0
        for ms in  self.massages:
            i+=1
            if  a == i:
                t = input("Ruxsat berasizmi\n(1) Ha (2) Yo'q \n--->")
                if t == "1":
                    user_id = ms.user_id
                    car_id = ms.car_id
                    date_start = input("Enter start date: ")
                    date_end = input("Enter end date: ")
                    order = Order(user_id, car_id, date_start, date_end)
                    self.orders.append(order)
                    count = 0
                    for car in self.cars:
                        count += 1
                        if count == car_id:
                            car.is_active = False
                    count = 0
                    for user in self.users:
                        count += 1
                        if count == user_id:
                            user.is_active = False

    def add_user(self):
        username = input("Enter username: ")
        phone =    input("Enter phone: ")
        seria =    input("Enter seria: ")
        age =      input("Enter age: ")
        password = input("Enter password: ")
        us = User(username,phone,seria,age,password)
        self.users.append(us)

    def add_car(self):
        model = input("Enter model: ")
        brand = input("Enter brand: ")
        year  = input("Enter year: ")
        seria = input("Enter seria: ")
        car = Car(model,brand,year,seria)
        self.cars.append(car)

    def show_all_cars(self):
        count = 0
        for car in self.cars:
            count += 1
            print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria}")

    def book_cars(self,username):
        usern_id = 0
        count = 0
        for user in self.users:
            count+=1
            if user.username == username:
                usern_id = count
        count = 0
        for car in self.cars:
            if car.is_active:
                count += 1
                print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria} ---")
        a = int(input("Enter an id: ")) - 1
        count = 0
        for car in self.cars:
            count+=1
            if count == a:
                s = Massage(usern_id,a)
                self.massages.append(s)

    def show_all_users(self):
        count = 0
        for user in self.users:
            count += 1
            print(f"{count}.{user.username} - {user.phone} - {user.seria} - {user.age}")

    def edit_user(self,username,password):
        for user1 in self.users:
            if user1.username == username and user1.password == password:
                user1.username = input("Enter new username: ")
                user1.phone    = input("Enter new phone: ")
                user1.seria    = input("Enter new seria: ")
                user1.age      = input("Enter new age: ")
                user1.password = input("Enter new password: ")

    def show_cars_not_users(self):
        count = 0
        for car in self.cars:
            if car.is_active:
                count+=1
                print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria}")

    def show_cars_in_users(self):
        count = 0
        for car in self.cars:
            if not car.is_active:
                count+=1
                print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria}")

    def show_working_users(self):
        count = 0
        for user in self.users:
            if not user.is_active:
                count+=1
                print(f"{count}.{user.username} - {user.phone} - {user.seria} - {user.age}")

    def make_order(self):
        print("-"*20)
        count1 = 0
        for car in self.cars:
            count1 += 1
            print(f"{count1}.{car.model} - {car.brand} - {car.year} - {car.seria}")
        print("="*20)
        count = 0
        for user in self.users:
            count += 1
            print(f"{count}.{user.username} - {user.phone} - {user.seria} - {user.age}")
        print("-" * 20)
        user_id    = int(input("Enter user ID: "))
        car_id     = int(input("Enter car ID: "))
        date_start = input("Enter start date: ")
        date_end   = input("Enter end date: ")
        order      = Order(user_id,car_id,date_start,date_end)
        self.orders.append(order)
        count = 0
        for car in self.cars:
            count+=1
            if count == car_id:
                car.is_active = False
        count = 0
        for user in self.users:
            count += 1
            if count == user_id:
                user.is_active = False

    def show_all_orders(self):
        count = 0
        for order in self.orders:
            count += 1
            user = self.users[order.user_id - 1]
            car = self.cars[order.car_id - 1]
            print(
                f"{count}. User: {user.username} | Car: {car.model} {car.brand} | From: {order.date_start} | To: {order.date_end}")

    def ignore_order(self):
        count = 0
        for order in self.orders:
            count += 1
            user = self.users[order.user_id - 1]
            car = self.cars[order.car_id - 1]
            print(
                f"{count}. User: {user.username} | Car: {car.model} {car.brand} | From: {order.date_start} | To: {order.date_end}")

        if count == 0:
            print("No orders found!")
            return

        n = int(input("Enter order number to ignore: "))

        if n < 1 or n > len(self.orders):
            print("Invalid order number!")
            return

        order = self.orders[n - 1]
        user = self.users[order.user_id - 1]
        car = self.cars[order.car_id - 1]

        user.is_active = True
        car.is_active = True

        self.orders.pop(n - 1)

        print("Order ignored successfully!")

    def login_screen(self):
        print("-" * 20)
        username = input(" Enter username: ")
        password = input(" Enter password: ")
        print("-" * 20)

        for user1 in self.users:
            if user1.username == username and user1.password == password:
                if user1.is_admin:
                    print("Welcome " + user1.username)
                    return 0,username,password
                else:
                    print("Welcome " + user1.username)
                    return 1,username,password

        return 2,username,password


park = Park("Park1")
admin = User("admin","12345",12345,22,"1111")
admin.is_admin = True
park.users.append(admin)

user = User("user","12345",12345,22,"1111")
park.users.append(user)

def park_manager(p:Park):
    while True:
        a,us,pa = p.login_screen()
        if a == 2:
            print("Username or password is incorrect please try again later !")
        elif a == 1:
            while True:
                print("User menu")
                b1 = input(" 1.Show cars \n 2.Change settings \n 3.Book a car\n 4.Exit\n --->")
                if b1 == "1":
                    p.show_cars_not_users()
                elif b1 == "2":
                    p.edit_user(us,pa)
                elif b1 == "3":
                    p.book_cars(us)
                else:
                    break
        elif a == 0:
            while True:
                print("Admin menu")
                b2 = input(" 1.Add menu\n 2.Show menu\n 3.Order menu\n 4.Show massages\n 5.Exit --->")
                if b2 == "1":
                    while True:
                        b3 = input(" 1.Add user\n 2.Add car\n 3.Exit\n --->")
                        if b3 == "1":
                            p.add_user()
                        elif b3 == "2":
                            p.add_car()
                        else:
                            break
                elif b2 == "2":
                    while True:
                        b3 = input(" 1.Show all users\n 2.Show working users\n 3.Show all cars\n 4.Show cars in users\n 5.Show orders\n 6.Exit \n --->")
                        if b3 == "1":
                            p.show_all_users()
                        elif b3 == "2":
                            p.show_working_users()
                        elif b3 == "3":
                            p.show_all_cars()
                        elif b3 == "4":
                            p.show_cars_in_users()
                        elif b3 == "5":
                            p.show_all_orders()
                        else:
                            break
                elif b2 == "3":
                    while True:
                        b3 = input(" 1.Make order\n 2.Ignore order\n 3.Exit\n --->")
                        if b3 == "1":
                            p.make_order()
                        elif b3 == "2":
                            p.ignore_order()
                        else:
                            break
                elif b2 == "4":
                    p.show_massages()
                else:
                    break


park_manager(park)