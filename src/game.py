"""
Main Game Class - Core Game Loop and State Management
"""

import pygame
import sys

from src.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GAME_STATE_LOBBY,
    GAME_STATE_MATCH, GAME_STATE_MATCH_OVER
)
from src.states.lobby import LobbyState
from src.states.match import MatchState
from src.states.match_over import MatchOverState


class OmniAssaultGame:
    """
    Main game class responsible for managing game loop,
    state transitions, and overall game flow.
    """
    
    def __init__(self, width, height, fps):
        """
        Initialize the game.
        
        Args:
            width: Screen width in pixels
            height: Screen height in pixels
            fps: Frames per second
        """
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        
        # Create display surface
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("OMNI ASSAULT: CROSS-GENRE HUB")
        
        # Initialize font
        pygame.font.init()
        
        # Game state management
        self.current_state = GAME_STATE_LOBBY
        self.states = {}
        self.current_game_mode = None
        
        # Initialize states
        self._init_states()
        
        # Running flag
        self.running = True
    
    def _init_states(self):
        """
        Initialize all game states.
        """
        self.states[GAME_STATE_LOBBY] = LobbyState(self)
        self.states[GAME_STATE_MATCH] = MatchState(self)
        self.states[GAME_STATE_MATCH_OVER] = MatchOverState(self)
    
    def change_state(self, new_state, game_mode=None):
        """
        Change to a new game state.
        
        Args:
            new_state: The state to change to
            game_mode: Game mode if transitioning to match state
        """
        if new_state in self.states:
            self.current_state = new_state
            self.current_game_mode = game_mode
            
            # Reinitialize state if needed
            if new_state == GAME_STATE_MATCH:
                self.states[GAME_STATE_MATCH].initialize(game_mode)
            elif new_state == GAME_STATE_LOBBY:
                self.states[GAME_STATE_LOBBY].reset()
    
    def handle_events(self):
        """
        Handle all events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                # Delegate to current state
                self.states[self.current_state].handle_event(event)
    
    def update(self, dt):
        """
        Update game logic.
        
        Args:
            dt: Delta time since last frame
        """
        self.states[self.current_state].update(dt)
    
    def draw(self):
        """
        Draw everything to the screen.
        """
        # Clear screen
        self.screen.fill((15, 15, 20))
        
        # Draw current state
        self.states[self.current_state].draw(self.screen)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """
        Main game loop.
        """
        while self.running:
            # Calculate delta time
            dt = self.clock.tick(self.fps) / 1000.0
            
            # Handle events
            self.handle_events()
            
            # Update
            self.update(dt)
            
            # Draw
            self.draw()
