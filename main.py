# main.py
from game_state import GameState
from ui import start_ui

state = GameState()

start_ui(state, apply_passive_items=None) 
