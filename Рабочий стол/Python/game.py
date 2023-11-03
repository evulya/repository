from typing import Optional, Self
import random
def check_positive_num(value: int|float, classes: tuple = (int, float)):
    if not isinstance(value, classes):
        classnames = [class_.__name__ for class_ in classes]
        raise TypeError(f'{type(value).__name__} is not in {classnames}')
    if value<0:
        raise ValueError(f'value {value} <0')
class Weapon:
    def __init__(self, title: str, damage: int|float):
        self.title, self.damage = title, damage
    @property
    def damage(self)-> int|float:
        return self.damage
    @damage.setter
    def damage(self, new_damage: int|float)-> None:
        check_positive_num(new_damage)
        self._damage = new_damage
expelled_students_weapon = Weapon('Venik', 0)
class Hero:
    attack_random =0.1
    def __init__(self, name:str, health: int|float =100,
                 weapon: Optional[Weapon] = None, attack: int|float = 10
                 )-> None:
        self.name, self.health, self.weapon = name, health, weapon
        self.__default_attack = attack
    @property
    def weapon(self)-> Weapon:
        return self._weapon
    @weapon.setter
    def weapon(self, new_weapon: Weapon)-> None:
        if new_weapon is None:
            self.weapon = None
            return
        if not isinstance(new_weapon, Weapon):
            raise TypeError(f'{type(new_weapon).__name__} is not a Weapon')
        self._weapon = new_weapon
    @property
    def health(self, new_health: int|float)->None:
        check_positive_num(new_health)
        self._health = new_health
    @property
    def damage(self)-> int|float:
        real_damage = self.weapon.damage if self.weapon else self.__default_attack
        delta = real_damage * self.__class__.attack_random
        return round(real_damage + random.uniform(-delta, delta),1)
    def pvp(self, other: Self)-> int:
        if not isinstance(other, type(self)):
            raise TypeError(f'Hero {self.name} cannot fight {type(other).__name__}')
        hero_weapon = f'with weapon {self.weapon.title}' if self.weapon else 'without weapon'
        print(f'Hero {self.name}{self.health}hp{hero_weapon}({self.damage} dmg)')
        other_weapon = f'with weapon {other.weapon.title}' if other.weapon else 'without_weapon'
        print(f'Hero {other.name}{other.health}hp {other_weapon}({other.damage}dmg)')
        hero_hp, other_hp = self.health, other.health
        while hero_hp > 0 and other_hp>0:
            hero_hp -=other.damage
            other_hp -= self.damage
        print(f'Result: {self.name} {hero_hp} hp; {other.name}{other_hp} hp')
        if hero_hp <= 0 and other_hp <=0:
            print('DRAW')
            return 0
        elif hero_hp <= 0:
            print(f'{other.name} victory!')
            return 2
        print(f'{other.name} victory!')
        return 1
    class Arena:
        draw_points=1
        victory_points = 3
        def __init__(self, heroes: list[Hero])-> None:
            self.heroes = heroes
        def check_hero(self, hero : Hero)-> None:
            if not isinstance(hero, Hero):
                raise TypeError(f'{type(hero).__name__} is not a Hero')
        def add_hero(self, hero: Hero)-> None:
            self.check_hero(hero)
            self._heroes.append(hero)
        def remove_hero(self, hero: Hero)-> None:
            self.check_hero
            if hero not in self._heroes:
                print(f'Hero {hero.name} is not present in Arena Heroes')
            self._heroes.remove(hero)
    @property
    def heroes(self)->list[Hero]:
        return self._heroes
    @heroes.setter
    def heroes(self, new_heroes: list[Hero])->None:
        for hero in new_heroes:
            self.check_hero(hero)
        self._heroes = new_heroes
    @heroes.setter
    def heroes(self, new_heroes: list[Hero])->None:
        for hero in new_heroes:
            self.check_hero(hero)
        self._heroes = new_heroes
    def start(self)->None:
        print('Please greet warmly our noble Arena Heroes!')
        for idx, hero in enumerate(self.heroes):
            hero_weapon=f'with weapon {hero.weapon.title}'if hero.weapon else 'without weapon'
            print(f'{idx+1}.{hero.name}{hero_weapon}({hero.damage} dmg)')
        
