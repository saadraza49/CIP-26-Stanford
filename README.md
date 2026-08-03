# 🎓 Stanford Code in Place (CIP 2026) — Section Leader Solutions

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Stanford CIP](https://img.shields.io/badge/Stanford-Code%20in%20Place-8C1515?style=for-the-badge)
![Section Leader](https://img.shields.io/badge/Role-Section%20Leader-gold?style=for-the-badge)
![Certificate Verified](https://img.shields.io/badge/LinkedIn-Certificate%20Verified-0A66C2?style=for-the-badge&logo=linkedin)

Welcome to the repository containing section teaching materials, problem walkthroughs, and solutions for **Stanford University's Code in Place (CIP 2026)**.

As a **Section Leader**, I had the privilege of mentoring and teaching a global section of **10 to 15 students from all around the world**, guiding them through foundational programming concepts in Python over a 6-week intensive program.

📜 **Official Section Leader Certificate**: [View LinkedIn Certificate Post](https://www.linkedin.com/posts/m-saadraza_codeinplace-stanford-python-share-7475260155933179905-nO7T/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFlReHwBCuLoLEkw83t8q6lxz1cna2GlLxg)

---

## 📚 6-Week Section Curriculum Overview

The curriculum spans **6 weeks**, moving progressively from visual logic and control flow with Karel the Robot to full-fledged Python console games, canvas graphics, data structures, and file I/O.

```
       ┌──────────────────────────────────────────────────────────┐
       │              CIP 2026 CURRICULUM ROADMAP                │
       └──────────────────────────┬───────────────────────────────┘
                                  │
      ├── Week 1: Control Flow & Function Decomposition (Karel)
      ├── Week 2: Advanced Karel Algorithms & State Management
      ├── Week 3: Console Python - Variables, Math & Decisions
      ├── Week 4: Randomization, Game Loops & Milestones
      ├── Week 5: Graphics, Canvas Geometry & Color Logic
      └── Week 6: Lists, File I/O & Interactive Word Games
```

---

## 📅 Detailed Weekly Breakdown & Teaching Content

### 🔹 Week 1: Control Flow & Decomposition with Karel
- **Focus**: Algorithmic problem-solving, structural decomposition, helper functions, and spatial orientation.
- **Concepts Taught**: `while` loops (`front_is_clear()`), conditional execution (`beepers_present()`), custom function abstraction (`build_hospital()`, `turn_right()`, `safe_move()`).
- **Featured Solution**:
  - [`W1_Hospital_Karel.py`](W1_Hospital_Karel.py): Instructs Karel to detect supply sites and construct multi-beeper hospital structures while traversing a grid safely.

---

### 🔹 Week 2: Advanced Karel & Algorithmic State Tracking
- **Focus**: State management using physical grid markers (beepers), nested loops, and non-trivial navigation.
- **Concepts Taught**: Two-way movement loops, state propagation (`spread()`), coordinate resetting, and returning to dynamic home positions.
- **Featured Solution**:
  - [`W2_Art_of_Karel.py`](W2_Art_of_Karel.py): Implements a beeper redistribution algorithm that moves stacks of beepers across grid positions using decomposed navigation functions (`return_to_the_pile()`, `go_to_empty_pile()`, `return_to_base()`).

---

### 🔹 Week 3: Console Python — Variables, Math & Control Flow
- **Focus**: Transition from Karel to native Python console programming, input/output handling, numeric types, and branch logic.
- **Concepts Taught**: Type casting (`str` to `float`), mathematical constants, formatted string literals (f-strings), `if-elif-else` conditional trees, and rounding numbers.
- **Featured Solutions**:
  - [`W3_Mars_Weight.py`](W3_Mars_Weight.py): Calculates equivalent body weight on Mars (`MARS_MULTIPLE = 0.378`) with user interaction and f-string formatting.
  - [`W3_Planetary_Weight.py`](W3_Planetary_Weight.py): Interactive solar system gravity calculator supporting Mercury, Venus, Mars, Jupiter, Saturn, Uranus, and Neptune with fallback validation for invalid inputs.

---

### 🔹 Week 4: Randomization, Game Loops & Milestone Development
- **Focus**: The `random` module, multi-round game state tracking, Boolean logic evaluation, and software milestone methodology.
- **Concepts Taught**: `random.randint()`, game loop mechanics, score accumulator patterns, boolean expression mapping (`higher_and_correct`), input validation loops, and performance feedback logic.
- **Featured Solutions**:
  - [`W4_High_Low_Game.py`](W4_High_Low_Game.py): Milestone-driven implementation of a multi-round High-Low guessing game against the computer.
  - [`W4_High_Low_Game_With_Extensions.py`](W4_High_Low_Game_With_Extensions.py): Extended version featuring input validation loops (`while choice not in ['higher', 'lower']`) and custom end-game evaluation tiers.

---

### 🔹 Week 5: Graphics, Canvas & Randomization
- **Focus**: Graphical User Interfaces (GUI) using Stanford's `graphics` library, 2D coordinate geometry, dynamic styling.
- **Concepts Taught**: Canvas bounds `(x1, y1, x2, y2)`, programmatic shape rendering (`create_oval`), randomized color choices, and spatial containment logic.
- **Featured Solution**:
  - [`W5_Random_Circles.py`](W5_Random_Circles.py): Renders dynamic, multi-colored circles on a 2D canvas with customizable palette selection (`random_color()`) and extension challenges for edge-bound positioning.

---

### 🔹 Week 6: Data Structures (Lists), File I/O & Interactive Games
- **Focus**: Python data structures (`list`), sequence indexing, list mutation, reading external files, and building complete terminal games.
- **Concepts Taught**: List creation and appending (`append()`), `len()` queries, random index sampling (`random.choice()`, `random.randint()`), file reading with `open()`, string whitespace sanitization (`strip()`), and game loops.
- **Featured Solutions**:
  - [`W6_List_Practice.py`](W6_List_Practice.py): Core list operations, element manipulation, and length evaluation.
  - [`W6_Index_Game.py`](W6_Index_Game.py): Interactive list index quiz prompting users to identify items at randomly selected indices.
  - [`W6_Heads_Up.py`](W6_Heads_Up.py): Terminal-based word guessing game that loads word banks from `cswords.txt`, cleans inputs, and presents endless random word prompts.

---

## 🛠️ How to Run the Solutions

Ensure you have **Python 3.x** installed. You can execute any section solution script directly from your terminal:

```bash
# Clone the repository
git clone https://github.com/saadraza49/CIP-26-Stanford.git
cd CIP-26-Stanford

# Run Console Programs (e.g., Week 4 High-Low Game)
python W4_High_Low_Game.py

# Run Graphical Programs (e.g., Week 5 Random Circles)
python W5_Random_Circles.py

# Run File I/O & List Games (e.g., Week 6 Heads Up)
python W6_Heads_Up.py
```

---

## 🤝 Teaching & Mentorship Philosophy

In Code in Place, section leaders don't just teach code syntax—we teach **computational thinking**, **debugging techniques**, **clean code habits**, and **confidence**. Every section meeting combined:
1. **Live Problem Walkthroughs**: Breaking down problems into small, achievable milestones.
2. **Interactive Pair Programming**: Encouraging students to talk through their logical reasoning.
3. **Extension Challenges**: Pushing students beyond the basic solution to explore real-world edge cases.

---

## 👨‍💻 Author & Section Leader

**Muhammad Saad Raza**  
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/m-saadraza/)  
- 📜 [Stanford CIP Section Leader Certificate Post](https://www.linkedin.com/posts/m-saadraza_codeinplace-stanford-python-share-7475260155933179905-nO7T/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFlReHwBCuLoLEkw83t8q6lxz1cna2GlLxg)  
- 🐙 [GitHub Profile](https://github.com/saadraza49)

---
*Created with ❤️ for Stanford Code in Place students across the globe.*