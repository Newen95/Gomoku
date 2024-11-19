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

    if command == "END":
        return "END"
    elif command == "START":
        return start_command(parts, state)
    elif command == "TURN":
        return turn_command(parts, state)
    elif command == "BEGIN":
        return begin_command(state)
    elif command == "BOARD":
        return board_command(parts, state)
    elif command == "INFO":
        return info_command(parts, state)
    elif command == "ABOUT":
        return "ABOUT"
    elif command == "PRINT":
        return print_command(state)
    elif command == "RESTART":
        return restart_game_command(state)
    elif command == "RECTSTART":
        return rectstart_command(parts, state)
    elif command == "TAKEBACK":
        return takeback_command(parts, state)
    elif command == "PLAY":
        return play_command(parts, state)
    else:
        return "ERROR: Unknown command"
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.restart()
    state.started = False
    return "OK: Game has been restarted."