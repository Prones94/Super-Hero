# superheroes.py
from random import randint, choice

# Ability Class


class Ability:
    def __init__(self, name, max_damage=0):
        self.name = name
        self.damage = max_damage

    def attack(self):
        '''Returns a value between 0 and value set by self.max_damage'''
        attack_power = randint(0, self.damage)
        return attack_power

# Weapoon Class inheriting from Ability class


class Weapon(Ability):
    def attack(self):
        wpn_atk = self.damage // 2
        return randint(wpn_atk, self.damage)

# Armor Class


class Armor:
    def __init__(self, name, max_block=0):
        self.name = name
        self.defense = max_block

    def block(self):
        '''Returns random value between 0 and value set by self.defense'''
        return randint(0, self.defense)


# Hero Class
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.health = starting_health
        self.current_health = self.health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_atk = 0
        for ability in self.abilities:
            total_atk += ability.attack()
        return total_atk

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        damage_amt = 0
        for armor in self.armors:
            damage_amt += armor.block()
        return damage_amt

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


    def fight(self, opponent):
        if not self.abilities:
            return 'Draw'
        while True:
            if self.is_alive():
                hero_attack = self.attack()
                opponent.take_damage(hero_attack)
            else:
                print(f'{opponent.name} won!')
                opponent.add_kill(1)
                self.add_death(1)
                break
            if opponent.is_alive():
                hero_attack = opponent.attack()
                self.take_damage(hero_attack)
            else:
                print(f'{self.name} won!')
                self.add_kill(1)
                opponent.add_death(1)
                break

# class of Team


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(self.remainder_heroes()[0]) < len(self.heroes) and len(other_team.remainder_heroes()[0]) < len(self.heroes):
            my_hero = choice(self.remainder_heroes()[1])
            opponent_hero  = choice(other_team.remainder_heroes()[1])
            my_hero.fight(opponent_hero)

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            kd_ratio = hero.kills / hero.deaths
            print(f'Kill/Death Ratio for {hero.name}: {kd_ratio}')

    def remainder_heroes(self):
        dead_hero = []
        alive_hero = []
        for hero in self.heroes:
            if hero.is_alive() == False:
                dead_hero.append(hero)
            else:
                alive_hero.append(hero)
        return dead_hero, alive_hero


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
