# git init - создание git репозитория
# git config user.name 'Ilgiz'
# git config user.email 'test@gmail.com'
# git add .
# git commit -m 'Создали модель человека : eat, work, act'

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.


from termcolor import cprint
import random
import time

class Human:

    def __init__(self, name):
        self.name = name 
        self.fullness = 50 
        self.house = None 

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'


    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 50
        self.fullness -= 10


    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} - поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'{self.name} - нет еды', color='red')
            self.shopping()


    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint(f'{self.name} - заселился в доме', color='green')


    def shopping(self):
        if self.house.money >= 50:
            cprint(f'{self.name} - пошёл в магазин за едой', color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} - кончились деньги', color='red')
            self.work()


    def watch_TV(self):
        cprint(f'{self.name} - Смотрит телевизор', color='green')
        self.fullness -= 10


    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} - умер ...', color='red')
            return
        dice = random.randint(1, 6)

        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_TV()
        



class House:
    
    def __init__(self):
        self.food = 50
        self.money = 0


    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'


house = House()
citizens = [
    Human(name='Бивис'),
    Human(name='Батхед'),
    Human(name='Кенни')
]

# Заселение объектов
for citizen in citizens:
    citizen.go_to_the_house(house)


for day in range(1,2):
    print(f'================= {day} =================')
    for citizen in citizens:
        time_act = random.randint(1, 2)
        time.sleep(time_act)
        citizen.act()
    print('--- Конец дня ---')
    for citizen in citizens:
        print(citizen)
        print(house) 



# Создадим трех людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должен быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.