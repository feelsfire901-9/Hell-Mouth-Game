# OMNI ASSAULT: CROSS-GENRE HUB

## Overview

A high-quality tactical multi-genre game hub built with Pygame. Experience three distinct game modes in one unified platform with a futuristic, Free Fire-inspired UI.

## Features

### Core Engine
- **Resolution**: 1150x800 pixels
- **Frame Rate**: 60 FPS
- **Graphics**: Dark futuristic theme with neon blue borders and gold accents
- **Platform**: Python-based with Pygame

### Game Modes

#### 1. Tower Domination (War Mode)
Strategic tower conquest gameplay where you capture and control tactical nodes.
- Capture enemy towers
- Generate units automatically
- Upgrade bases for better production
- **Objective**: Eliminate all enemy towers

#### 2. Village Forge (Base Builder)
Clash of Clans-inspired base building and defense mode.
- Manage town halls and defensive structures
- Gold mining and resource management
- Defend against waves of attacks
- **Objective**: Destroy enemy town hall

#### 3. Epic Clash (Hero MOBA)
MOBA-style lane-based gameplay with strategic positioning.
- Three lanes to control
- Ancient structures to defend
- Hero movement and positioning
- **Objective**: Destroy enemy ancient

### Player Mechanics
- **Movement**: WASD or Arrow Keys
- **Upgrades**: Press 'U' near friendly bases (40 credits)
- **Resources**: Collect credits from gameplay
- **Health System**: Monitor hero health and bases

### UI Elements
- **Top Panel**: Current mode and match information
- **Right Sidebar**: Tactical commands and upgrade instructions
- **Bottom Dashboard**: Credits wallet, skills panel, and combat information
- **Animated Borders**: Dynamic neon effects

## Installation

### Requirements
- Python 3.7+
- Pygame 2.5.2+

### Setup

1. Clone the repository
```bash
git clone https://github.com/feelsfire901-9/Hell-Mouth-Game.git
cd Hell-Mouth-Game
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the game
```bash
python main.py
```

## Project Structure

```
Hell-Mouth-Game/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md              # Documentation
└── src/
    ├── __init__.py
    ├── constants.py        # Game constants
    ├── colors.py          # Color palette
    ├── game.py            # Main game class
    ├── states/            # Game states
    │   ├── base_state.py
    │   ├── lobby.py
    │   ├── match.py
    │   └── match_over.py
    ├── game_modes/        # Game mode implementations
    │   ├── base_mode.py
    │   ├── tower_domination.py
    │   ├── village_forge.py
    │   └── epic_clash.py
    ├── entities/          # Game entities
    │   ├── hero.py
    │   ├── tower.py
    │   ├── projectile.py
    │   ├── tactical_node.py
    │   ├── building.py
    │   └── lane_turret.py
    └── ui/                # UI components
        ├── button.py
        ├── panel.py
        └── hud.py
```

## Game Flow

### Lobby State
1. Select a game mode from three options
2. View your squad information
3. Click "LAUNCH SIMULATION" to start

### Match State
1. Control your hero with WASD or Arrow Keys
2. Manage bases and upgrades
3. Complete mode-specific objectives
4. Win by meeting victory conditions

### Match Over State
1. View results (Victory/Mission Failure)
2. Click "RETURN TO HUB" to go back to lobby

## Controls

| Key | Action |
|-----|--------|
| W | Move Up |
| A | Move Left |
| S | Move Down |
| D | Move Right |
| Arrow Keys | Alternative Movement |
| U | Upgrade Nearby Base |
| Mouse | UI Navigation |

## Victory Conditions

### Tower Domination
- Capture all enemy towers

### Village Forge
- Destroy enemy town hall

### Epic Clash
- Destroy enemy ancient structure

## Architecture

### Design Patterns
- **State Pattern**: Game state management
- **Entity Pattern**: Game objects and entities
- **Observer Pattern**: Event handling
- **MVC Pattern**: Separation of logic and rendering

### Code Quality
- Object-oriented design
- Comprehensive documentation
- Modular structure
- Clean separation of concerns

## Performance
- Optimized for 60 FPS
- Efficient collision detection
- Minimal memory footprint
- Smooth animations

## Future Enhancements
- Multiplayer support
- Additional game modes
- Advanced AI opponents
- Sound and music system
- Particle effects
- Leaderboards
- Campaign mode

## License

This project is open source and available under the MIT License.

## Credits

Developed as a comprehensive Pygame game framework demonstrating professional game development practices.

---

**OMNI ASSAULT: CROSS-GENRE HUB** - Where tactical gameplay meets futuristic aesthetics.
