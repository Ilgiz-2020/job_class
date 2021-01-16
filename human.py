
from termcolor import cprint
import random


class Human:

    def __init__(self, name):
        self.name = name 
        self.fullness = 50 
        self.house = None 
        self.action = False


    def __str__(self):
        return f'Я - {self.name}, сытость {self.fullness}'


    def work(self):
        cprint(f'{self.name} сходил на работу', color='blue')
        self.house.money += 50
        self.fullness -= 10


    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} - поел', color='yellow')
            self.fullness += 20
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
        
        self.dice = random.randint(1, 6)

        if self.fullness < 30:
            self.action = True
            self.eat()
        elif self.house.food < 20:
            self.action = True
            self.shopping()
        elif self.house.money <= 50:
            self.action = True
            self.work()
        elif self.dice == 1:
            self.work()
        elif self.dice == 2:
            self.eat()
        elif self.dice == 3:
            self.watch_TV()
