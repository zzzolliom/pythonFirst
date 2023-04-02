"""Написать класс Character обладает 3-мя характеристаки : атака, здоровье, уклонение
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}
"""
from random import randint
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}
class Character():   #класс
    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self,char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def assign_atributer(self):
        types_dict = TYPES[self._char_type]
        self._health=types_dict['health']
        self._attack=types_dict['attack']
        self._dodge=types_dict['dodge']
    def attack(self,object):
        self.attack()


    def dodge_sucsess(self,_attack,_dodge):
        number=random.randint(0, 100)
        if number <_dodge or number == _dodge:
            for i in range(self._dodge):
            if _attack > _dodge:
                self._dodge-=1
                self. _attack-=1

    def take_damage(self,damage):
        self._health -= damage




    def is_dead(self):
        pass
