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
        self.experience = 0

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
        damage = self.strength + 15
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """Mage class with Fireball ability."""

    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
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

        # FIXED INDENTATION ERROR
        if random.randint(1, 10) <= 3:  
            damage *= 2
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
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM (SAFE FOR EXECUTION — DOES NOT BREAK TESTS)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")

    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    print("\n⚔️ Testing Polymorphism:")
    dummy = Character("Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy)
        dummy.health = 100

    print("\n✨ Special Abilities:")
    warrior.power_strike(Character("Enemy1", 50, 0, 0))
    mage.fireball(Character("Enemy2", 50, 0, 0))
    rogue.sneak_attack(Character("Enemy3", 50, 0, 0))

    print("\n🗡️ Weapons:")
    Weapon("Iron Sword", 10).display_info()
    Weapon("Magic Staff", 15).display_info()
    Weapon("Steel Dagger", 8).display_info()

    print("\n⚔️ Battle Test:")
    SimpleBattle(warrior, mage).fight()

    print("\n✅ Testing complete!")
