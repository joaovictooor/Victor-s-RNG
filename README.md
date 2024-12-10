# Battle Game - README

## Table of Contents
1. [Overview](#overview)
2. [Game Components](#game-components)
3. [How to Play](#how-to-play)
4. [Battle Mechanics](#battle-mechanics)
5. [Inventory System](#inventory-system)
6. [Healing with Fruits](#healing-with-fruits)
7. [Winning and Losing](#winning-and-losing)

---

## Overview
This is a turn-based battle game where players manage a collection of characters and items to defeat enemies in combat. Each character has unique stats, and players must strategize to maximize their chances of survival and victory.

---

## Game Components

### Characters
Characters have the following attributes:
- **Health**: Determines how much damage a character can take before being defeated.
- **Attack**: Determines how much damage a character deals to enemies.

Characters can be unlocked and used for battles. They can also be lost permanently if defeated in combat.

### Items
- **Fruits**: Special healing items used during battles to recover health. Limited in quantity.

### Points
- **Roll Points**: Earned by winning battles. Used to unlock new characters or items.

---

## How to Play
1. **Start the Game**: The player begins with a limited set of characters and items.
2. **Choose a Character**: Before each battle, select a character from your inventory to fight.
3. **Battle**: Engage in turn-based combat with an enemy character.
4. **Win or Lose**: Gain rewards for victories or suffer penalties for defeats.

---

## Battle Mechanics
- The game pits one player-controlled character against a randomly generated enemy.
- Both sides take turns attacking.
- Damage dealt is subtracted from the opponent's health.
- The battle continues until one side's health reaches zero.

### Special Rules
- Damage taken triggers the option to use healing items (if available).
- Healing restores up to half the character's current health (rounded to the nearest whole number) without exceeding the character's maximum health.

---

## Inventory System
The inventory includes:
1. **Characters**: Displays all available characters and their quantities.
2. **Fruits**: Tracks the number of fruits available for healing during battles.

Characters and items are shown in a numbered list for easy selection.

### Inventory Rules
- Players cannot select fruits as their active character.
- Defeated characters are removed from the inventory.
- Fruits are consumed when used.

---

## Healing with Fruits
1. **Trigger**: After taking damage, the player is prompted to use a fruit (if available).
2. **Usage**:
   - Reduces the fruit count by one.
   - Restores half the character's current health.
   - If the healing exceeds the maximum health, the character is fully healed, and excess healing is discarded.
3. **Limits**: If no fruits are available, healing is not possible.

---

## Winning and Losing
### Victory
- Defeat the enemy to win the battle.
- Earn 3 Roll Points for each victory.

### Defeat
- If your character's health drops to zero:
  - The character is removed from the inventory.
  - Lose 1 Roll Point (if you have any).

### Game Over
- If no characters remain in the inventory, the game ends.

