class User:
    def __init__(self, username, phone, seria, age, password):
        self.username = username
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = password
        self.is_active = False
        self.is_admin = False


class Car:
    def __init__(self, model, brand, year, seria, ):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = False

class Order:
    def __init__(self,user_id,car_id,date_start,date_end):
        self.user_id =user_id
        self.car_id =car_id
        self.date_start =date_start
        self.date_end =date_end
        self.is_active = True

class Park:
    def __init__(self,title):
        self.title =title
        self.users  =[]
        self.cars  =[]
        self.orders  =[]

    def show_all_cars(self):
        count = 0
        for car in self.cars:
            count += 1
            print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria}")

    def show_all_users(self):
        count = 0
        for user in self.users:
            count += 1
            print(f"{count}.{user.username} - {user.phone} - {user.seria} - {user.age}")

    def show_cars_in_users(self):
        count = 0
        for car in self.cars:
            if car.is_active:
                count+=1
                print(f"{count}.{car.model} - {car.brand} - {car.year} - {car.seria}")

    def show_working_users(self):
        count = 0
        for user in self.users:
            if user.is_active:
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

    def make_order(self):
        pass

park = Park("Park1")
admin = User("admin","12345",12345,22,1111)
admin.is_admin = True
park.users.append(admin)

def park_manager(p:Park):
    pass

park_manager(park)