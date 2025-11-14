"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Maxwell Irving
Date: 11/14

AI Usage: AI helped correct indentation errors and remove TODO syntax issues.
"""

import random  # Used for Rogue's critical hit chance

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# CHARACTER SYSTEM IMPLEMENTATION
# ============================================================================

class Character:
    """Base class for all characters."""

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        # AI Concept: State update — reflects internal agent state change
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health now: {self.health}")

    def display_stats(self):
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")


class Player(Character):
    """Intermediate class for player-controlled characters."""

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0  # AI Concept: Learning metric — tracks agent progress

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience}")


class Warrior(Player):
    """Warrior class with Power Strike ability."""

    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        damage = self.strength + 5
        print(f"{self.name} performs a Warrior attack for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        # AI Concept: Rule-based decision — triggers enhanced action
        damage = self.strength + 15
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """Mage class with Fireball ability."""

    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        # AI Concept: Polymorphism — behavior changes based on class type
        damage = self.magic
        print(f"{self.name} casts a magic attack for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        damage = self.magic + 20
        print(f"{self.name} casts Fireball on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    """Rogue class with critical hit chance & Sneak Attack."""

    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        damage = self.strength
        if random.randint(1, 10) <= 3:
            damage *= 2
            # AI Concept: Stochastic behavior — introduces randomness into decision-making
            print(f"CRITICAL HIT! {self.name} attacks for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def sneak_attack(self, target):
        damage = self.strength * 2
        print(f"{self.name} performs Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """Weapon used via composition."""

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus  # AI Concept: Modular enhancement — external tool integration

    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")


class SimpleBattle:
    """Simulates a basic turn-based battle between two characters."""

    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def fight(self):
        # AI Concept: Agent interaction loop — simulates turn-based decision-making
        print(f"\nBattle Start: {self.char1.name} vs {self.char2.name}")
        while self.char1.health > 0 and self.char2.health > 0:
            self.char1.attack(self.char2)
            if self.char2.health <= 0:
                print(f"{self.char2.name} has been defeated!")
                break
            self.char2.attack(self.char1)
            if self.char1.health <= 0:
                print(f"{self.char1.name} has been defeated!")
                break
        print("Battle Over.")



