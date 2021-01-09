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

class Human:

    def __init__(self, name):
        self.name = name 
        self.fullness = 50 
        self.house = None 

    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'


    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.money += 50
        self.fullness -= 10


    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} - поел', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint(f'{self.name} - нет еды', color='red')


    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} - умер ...', color='red')
            return
        dice = random.randint(1, 6)
        if dice == 1:
            self.work()
        elif dice == 2:
            pass
        



class House:
    
    def __init__(self):
        self.food = 50
        self.money = 0


    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'


    


# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должен быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.