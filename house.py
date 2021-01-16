

class House:
    
    def __init__(self):
        self.food = 50
        self.money = 0


    def __str__(self):
        return f'В доме еды осталось {self.food}, денег осталось {self.money}'
