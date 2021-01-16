# git init - создание git репозитория
# git config user.name 'Ilgiz'
# git config user.email 'test@gmail.com'
# git add .
# git reset - 
# git commit -m 'Создали модель человека : eat, work, act'

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.


from termcolor import cprint
import random
import time



from programmer import Programmer
from smm import SMM 
from gamer import Gamer 
from house import House


citizens = [
    Programmer(name='Бивис'),
    SMM(name='Батхед'),
    Gamer(name='Кенни')
]

# Заселение объектов
for citizen in citizens:
    citizen.go_to_the_house(House())


for day in range(1,10):
    print(f'================= {day} =================')
    for citizen in citizens:
        time_act = random.randint(1, 2)
        time.sleep(time_act)
        citizen.act()
        citizen.action = False
    print('--- Конец дня ---')
    for citizen in citizens:
        print(citizen)
        print(citizen.house)
        # print(house) 



# Создадим трех людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должен быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.