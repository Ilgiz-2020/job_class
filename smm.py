from termcolor import cprint
import random
from human import Human


class SMM(Human):
    def write_post(self):
        cprint(f'{self.name} - пишет пост для Facebook', color='green')
        self.fullness -= 10

    def picture(self):
        cprint(f'{self.name} - готовит картинку для поста на Facebook', color='blue')
        self.house.money += 50
        self.fullness -= 20

    def stories(self):
        cprint(f'{self.name} - снимает сторис для Instagram', color='green')
        self.fullness -= 10

    def act(self):
        super().act()
        if self.action == False and self.fullness >= 10:
            if self.dice == 4:
                self.write_post()
            elif self.dice == 5:
                self.picture()
            elif self.dice == 6:
                self.stories()
