class Equipment:
    def __init__(self, weight):
        self.weight = weight
class Ball(Equipment):
    __sport_weight = {'volleyball': 250, 
                      'football': 450, 
                      'basketball': 650}
    __default_weight = 500
    def __init__(self, size, sport):
        weight = self.__class__.__sport_weight.get(sport)
        super().__init__(weight if weight else self.__class__.__default_weight)
        self.size = size
        self.sport = sport
korenyakin = Ball(50, 'football')
print(korenyakin.weight)
class Person:
    def __init__(self, name: str, age:int)