from termcolor import cprint
import random
from human import Human


class Gamer(Human):
    def train(self):
        cprint(f'{self.name} - тренируется', color='green')
        self.fullness -= 10

    def championship(self):
        cprint(f'{self.name} - участвует в чемпионате по Dota2', color='blue')
        self.house.money += 50
        self.fullness -= 20

    def learn(self):
        cprint(f'{self.name} - изучает теорию игр', color='green')
        self.fullness -= 10

    def act(self):
        super().act()
        if self.action == False and self.fullness >= 10:
            if self.dice == 4:
                self.train()
            elif self.dice == 5:
                self.championship()
            elif self.dice == 6:
                self.learn()