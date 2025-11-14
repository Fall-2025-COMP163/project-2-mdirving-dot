"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Maxwell Irving]
Date: [11/14

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
import random

# ============================================================================
# CHARACTER SYSTEM IMPLEMENTATION
# ============================================================================

class Character:
    """
    Base class for all characters.
    Defines core attributes and methods shared by all character types.
    """

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None  # Composition: characters can have a weapon

    def attack(self, target):
        """
        Basic attack using strength + optional weapon bonus.
        """
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces health by damage amount, ensuring it doesn't go below 0.
        """
        self.health = max(self.health - damage, 0)
        print(f"{self.name} takes {damage} damage. Health now: {self.health}")

    def display_stats(self):
        """
        Displays core character stats.
        """
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


class Player(Character):
    """
    Base class for player-controlled characters.
    Adds RPG-style attributes like class, level, and experience.
    """

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """
        Displays both base and player-specific stats.
        """
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience}")


class Warrior(Player):
    """
    Warrior class: high strength and health, low magic.
    Special ability: Power Strike.
    """

    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        """
        Overrides base attack with extra physical damage.
        """
        damage = self.strength + 5 + (self.weapon.damage_bonus if self.weapon else 0)
        print(f"{self.name} performs a Warrior attack for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Warrior's special move: deals double strength damage.
        """
        damage = self.strength * 2
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """
    Mage class: high magic, low strength and health.
    Special ability: Fireball.
    """

    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        """
        Overrides base attack to use magic instead of strength.
        """
        damage = self.magic + (self.weapon.damage_bonus if self.weapon else 0)
        print(f"{self.name} casts a magic attack for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """
        Mage's special move: deals double magic damage.
        """
        damage = self.magic * 2
        print(f"{self.name} casts Fireball on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    """
    Rogue class: balanced stats, chance-based critical hits.
    Special ability: Sneak Attack.
    """

    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        """
        Overrides base attack with a chance for critical hit.
        """
        crit = random.randint(1, 10) <= 3  # 30% crit chance
        base = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        damage = base * 2 if crit else base
        print(f"{self.name} attacks with{' a CRITICAL HIT!' if crit else ''} for {damage} damage!")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Rogue's special move: guaranteed critical hit using strength + magic.
        """
        damage = (self.strength + self.magic) * 2
        print(f"{self.name} performs Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """
    Weapon class used via composition.
    Characters can equip weapons to boost damage.
    """

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """
        Displays weapon name and bonus damage.
        """
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

