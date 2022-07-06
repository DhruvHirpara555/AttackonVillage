# Attack On Village

It is terminal based game inspired from clash of clans.

## Directory Structure

```bash
├── game.py
├── Readme.md
├── replay
│   ├── qq
│   └── wq
├── replay.py
└── src
    ├── buildings
    │   ├── buildings.py
    │   ├── cannons.py
    │   ├── huts.py
    │   ├── townhall.py
    │   └── walls.py
    ├── input.py
    ├── objects_game.py
    ├── screen.py
    └── troops
        ├── barbarian.py
        ├── king.py
        └── troops.py

4 directories, 16 files
```

## Instructions to Run

**Note:** Run the game only when terminal is in full screen 

### 1. Install all dependencies using following command

```bash
pip install colorama
```

```bash
pip install numpy
```

### 2. Run The Game

```bash
python3 game.py
```

### 3. Replay

At the end of each game you will be asked to enter filename to save replay with the file name given by you

To replay the game run

```bash
python3 replay.py
```

## How to Play

* W,A,S,D - For movement of King Or Queen
* [SPACE] for normal king or Queen attack
* "L" for special king or queen attack 
- 1, 2, 3 to spawn barbarians from spawning points corresponding to the key
- 4,5,6 to spawn archers from spawning points corresponding to the key
- 7,8,9 to spawn balloons from spawning points corresponding to the key
* R - Rage Spell H - Heal spell
