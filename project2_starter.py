"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Maxwell Irving]
Date: [11/14

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

import random  # Used for Rogue's critical hit chance

# ============================================================================
# CHARACTER SYSTEM IMPLEMENTATION
# ============================================================================

class Character:
    """
    Base class for all characters.
    Defines core attributes and methods shared by all character types.
    """

    def __init__(self, name, health, strength, magic):
        # Basic character stats
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None  # Composition: characters can equip a Weapon object

    def attack(self, target):
        """
        Basic attack method.
        Damage is based on strength plus weapon bonus (if equipped).
        """
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces health by damage amount.
        Ensures health doesn't drop below 0.
        """
        self.health = max(self.health - damage, 0)
        print(f"{self.name} takes {damage} damage. Health now: {self.health}")

    def display_stats(self):
        """
        Displays basic character stats.
        """
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


class Player(Character):
    """
    Intermediate class for player-controlled characters.
    Inherits from Character and adds RPG-style attributes.
    """

    def __init__(self, name, character_class, health, strength, magic):
        # Call parent constructor to initialize base stats
        super().__init__(name, health, strength, magic)
        self.character_class = character_class  # e.g., "Warrior", "Mage", "Rogue"
        self.level = 1  # Starting level
        self.experience = 0  # Starting XP

    def display_stats(self):
        """
        Displays both base stats and player-specific info.
        Overrides Character.display_stats().
        """
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience}")


class Warrior(Player):
    """
    Warrior class: high strength and health, low magic.
    Special ability: Power Strike.
    """

    def __init__(self, name):
        # Initialize with Warrior-specific stats
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        """
        Overrides base attack with extra physical damage.
        Adds +5 bonus to strength.
        """
        damage = self.strength + 5 + (self.weapon.damage_bonus if self.weapon else 0)
        print(f"{self.name} performs a Warrior attack for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Warrior's special move.
        Deals double strength as damage.
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
        # Initialize with Mage-specific stats
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
        Mage's special move.
        Deals double magic as damage.
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
        # Initialize with Rogue-specific stats
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        """
        Overrides base attack with a chance for critical hit.
        30% chance to deal double damage.
        """
        crit = random.randint(1, 10) <= 3  # Random chance for crit
        base = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        damage = base * 2 if crit else base
        print(f"{self.name} attacks with{' a CRITICAL HIT!' if crit else ''} for {damage} damage!")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Rogue's special move.
        Guaranteed critical hit using strength + magic.
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
        # Weapon has a name and a damage bonus
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """
        Displays weapon name and bonus damage.
        """
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

