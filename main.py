#!/usr/bin/env python3
"""
OMNI ASSAULT: CROSS-GENRE HUB
A high-quality tactical multi-genre game hub built with Pygame.

Author: Game Development Team
Version: 1.0.0
"""

import pygame
import sys
import os

from src.game import OmniAssaultGame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


def main():
    """
    Main entry point for the game application.
    Initializes Pygame and runs the game loop.
    """
    # Initialize Pygame
    pygame.init()
    
    # Create game instance
    game = OmniAssaultGame(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    
    # Run the game
    game.run()
    
    # Cleanup
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
