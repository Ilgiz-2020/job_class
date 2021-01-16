from termcolor import cprint
import random
from human import Human


class Programmer(Human):
    def work(self):
        super().work()
        self.house.money += 150
        self.fullness -= 20

    
    def watch_youtube(self):
        cprint(f'{self.name} - Смотрит Youtube', color='green')
        self.fullness -= 10


    def freelance(self):
        cprint(f'{self.name} - зашёл на фриланс', color='blue')
        self.house.money += 50
        self.fullness -= 30


    def play_game(self):
        cprint(f'{self.name} - весь день играл в игры', color='green')
        self.fullness -= 10


    def act(self):
        super().act()
        if not self.action and self.fullness >= 10: 
            if self.dice == 4:
                self.watch_youtube()
            elif self.dice == 5:
                self.freelance()
            elif self.dice == 6:
                self.play_game()