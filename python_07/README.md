
## INTRODUCTION
    DataDeck is a small project designed to teach you object-oriented programming by building a simple trading card game engine step by step. You 
    start by creating an abstract Card base class that defines common behavior for all cards, then add concrete types like creatures, spells, and 
    artifacts that share the same interface through polymorphism. As the exercises progress, you manage cards inside decks, implement sorting and 
    game logic, and finally add multiple inheritance with combat and magic abilities. The cards are just a theme—the real goal is to practice 
    clean architecture, abstraction, inheritance, interfaces, and writing modular, reusable Python code like you would in a real software project.

## Exercises Overview

### Exercise 0 — Card Foundation
Master abstract base classes and create the universal card blueprint.
Design an abstract `Card` class that defines the contract all cards must follow,
then implement your first concrete card type: `CreatureCard`.

**Key Concepts:** Abstract Base Classes (ABC), inheritance, abstract methods

---

### Exercise 1 — Deck Builder
Implement multiple concrete card types that all respect the same interface.
Build `SpellCard`, `ArtifactCard`, and a complete `Deck` management system
that works with any card type through polymorphism.

**Key Concepts:** Polymorphism, concrete implementations, class hierarchies

---

### Exercise 2 — Ability System
Design multiple abstract interfaces using composition and multiple inheritance.
Create `Combatable` and `Magical` interfaces, then build an `EliteCard`
that simultaneously implements multiple abilities.

**Key Concepts:** Multiple interfaces, multiple inheritance, interface composition

---

### Exercise 3 — Game Engine
Build a sophisticated game engine using Abstract Factory and Strategy Patterns.
Create `GameStrategy` and `CardFactory` interfaces with concrete implementations
like `AggressiveStrategy` and `FantasyCardFactory`.

**Key Concepts:** Abstract Factory Pattern, Strategy Pattern, composition over inheritance

---

### Exercise 4 — Tournament Platform
Combine everything into a unified tournament management system.
Build `Rankable` interface and `TournamentCard` with tournament capabilities,
then create a `TournamentPlatform` that manages matches, rankings, and leaderboards.

**Key Concepts:** Advanced composition, ranking systems, tournament management

---
