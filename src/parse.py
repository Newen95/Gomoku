##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## parse
##

from src.command.about import about_command  
from src.command.begin import begin_command
from src.command.board import board_command
from src.command.info import info_command
from src.command.play import play_command
from src.command.rectstart import rectstart_command
from src.command.restart import restart_game_command
from src.command.start import start_command
from src.command.takeback import takeback_command
from src.command.turn import turn_command

def print_command(state):
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.print_map()
    return "PRINT"

def parse(enter, state):
    parts = enter.strip().split()
    command = parts[0].upper() if parts else ""
    
    command_action = {
        "END": lambda: "END",
        "START": lambda: start_command(parts, state),
        "TURN": lambda: turn_command(parts, state),
        "BEGIN": lambda: begin_command(state),
        "BOARD": lambda: board_command(parts, state),
        "INFO": lambda: info_command(parts, state),
        "ABOUT": lambda: about_command(),
        "PRINT": lambda: print_command(state),
        "RESTART": lambda: restart_game_command(state),
        "RECTSTART": lambda: rectstart_command(parts, state),
        "TAKEBACK": lambda: takeback_command(parts, state),
        "PLAY": lambda: play_command(parts, state),
    }
    
    action = command_action.get(command, lambda: "ERROR: Unknown command")
    result = action()
    
    return result
