"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Maxwell Irving]
Date: [11/14

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

import random  # Used for Rogue's critical hit chance
# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
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
    
    def attack(self, target):
        """
        Basic attack method.
        Damage is based on strength plus weapon bonus (if equipped).
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces health by damage amount.
        Ensures health doesn't drop below 0.
        """
        self.health = max(0, self.health - damage)
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
        damage = self.strength + 5
        print(f"{self.name} performs a Warrior attack for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """
        Warrior's special move.
        Deals extra damage.
        """
        damage = self.strength + 15
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
        damage = self.magic
        print(f"{self.name} casts a magic attack for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """
        Mage's special move.
        Deals extra magic/damage.
        """
        damage = self.magic + 20
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
        damage = self.strength
         if random.randint(1, 10) <= 3:  # Random chance for crit
            damage *= 2
            print(f" CRITICAL HIT! {self.name} attacks for {damage} damage!")
         else:
              print(f"{self.name} attacks {target.name} for {damage} damage!")
             
        target.take_damage(damage)

    def sneak_attack(self, target):
        """
        Rogue's special move.
        Guaranteed critical hit using strength
        """
        damage = self.strength * 2
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
# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    TODO: Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    TODO: Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    TODO: Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
     
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
     
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    TODO: Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
     
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    TODO: Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
