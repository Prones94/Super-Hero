# superheroes.py
import random

# Ability Class

class Ability:
    def __init__(self,name,max_damage=0):
        self.name = name
        self.damage = max_damage
    
    def attack(self):
        '''Returns a value between 0 and value set by self.max_damage'''
        attack_power = random.randint(0,self.damage)
        return attack_power

# Armor Class
class Armor:
    def __init__(self,name,max_block=0):
        self.name = name
        self.defense = max_block

    def block(self):
        '''Returns random value between 0 and value set by self.defense'''
        armour = random.randint(0,self.defense)
        return armour

# Hero Class
class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.health = starting_health
        self.current_health = starting_health
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
        defense = self.defend()
        self.current_health = damage - defense

    def is_alive(self):
        pass

    def fight(self,Hero):
        pass

if __name__ == "__main__":
    # ability1 = Ability('Debugging Ability',900)
    # ability2 = Ability('Hacking Ability',900)
    armor1 = Armor('Shield',100)
    hero = Hero("Ash Ketchum", 500)
    hero.add_armor(armor1)
    print(hero.current_health)
    hero.take_damage(50)
    print(hero.current_health)
