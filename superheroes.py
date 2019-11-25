# superheroes.py
from random import randint, choice

# Ability Class

class Ability:
    def __init__(self,name,max_damage=0):
        self.name = name
        self.damage = max_damage
    
    def attack(self):
        '''Returns a value between 0 and value set by self.max_damage'''
        attack_power = randint(0,self.damage)
        return attack_power

# Armor Class
class Armor:
    def __init__(self,name,max_block=0):
        self.name = name
        self.defense = max_block

    def block(self):
        '''Returns random value between 0 and value set by self.defense'''
        return randint(0,self.defense)

# Hero Class
class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.health = starting_health
        self.current_health = self.health
        self.abilities = list()
        self.armors = list()

    def add_ability(self,ability):
        self.abilities.append(ability)

    def attack(self):
        total_atk = 0
        for ability in self.abilities:
            total_atk += ability.attack()
        return total_atk

    def add_armor(self,armor):
        self.armors.append(armor)

    def defend(self):
        damage_amt = 0
        for armor in self.armors:
            damage_amt += armor.block()
        return damage_amt

    def take_damage(self,damage):
        self.current_health -= damage - self.defend() 

    def is_alive(self):
        return self.current_health > 0

    def fight(self,opponent):
        if not self.abilities:
            return 'Draw'
        while True:
            if self.is_alive():
                hero_attack = self.attack()
                opponent.take_damage(hero_attack)
            else:
                print(f'{opponent.name} won!')
                break
            if opponent.is_alive():
                hero_attack = opponent.attack()
                self.take_damage(hero_attack)
            else:
                print(f'{self.name} won!')
                break

        


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 20)
    ability2 = Ability("Super Eyes", 10)
    ability3 = Ability("Wizard Wand", 800)
    ability4 = Ability("Wizard Beard", 2000)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    hero2.fight(hero1)
