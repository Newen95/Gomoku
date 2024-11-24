## ## EPITECH PROJECT, 2024
## Gomoku
## File description:
## ai

import random
import copy

"""
    Access point to heuristic function to give a score to the base move based on most valuable pattern in game
    
    Args:
        map: The current game board.
        player: The player for whom the heuristic is being calculated.
        opponent:  The opponent for whom the heuristic is being calculated.
"""
def heuristic_computation(map, player, opponent):
    score = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == player:
                score += win_score(map, x, y, player, opponent)
            elif map[y][x] == opponent:
                score -= win_score(map, x, y, opponent, player)
    return score
    
"""
    Computes the score to find the best move best on patern alignment.

    Args:
        map: The current game board.
        x: The x-coordinate of the position being evaluated.
        y: The y-coordinate of the position being evaluated.
        player: The player for whom the score is being calculated.
        opponent: The opponent for whom the score is being calculated.
"""
def win_score(map, x, y, player, opponent):
    score = 0

    for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        player_count = 0
        blocks = 0
        opponent_count = 0
        for step in range(-4, 3):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= ny < len(map) and 0 <= nx < len(map[0]):
                if map[ny][nx] == player:
                    player_count += 1
                elif map[ny][nx] == opponent:
                    opponent_count += 1
                elif map[ny][nx] == 0:
                    pass
                else:
                    blocks += 1
        if player_count >= 5:
            score += 10000
        elif opponent_count == 4 and blocks == 0:
            score += 1000
        elif player_count == 4 and blocks == 0:
            score += 800
        elif opponent_count == 3 and blocks == 0:
            score += 100
        elif player_count == 3 and blocks == 0:
            score += 80
        elif player_count == 2 and blocks == 0:
            score += 10
        elif player_count == 1 and blocks == 0:
            score += 1
        if player_count == 4 and blocks == 1:
            score += 5000
        elif player_count == 3 and blocks == 1:
            score += 500
    return score

"""
    Retrieves all possible moves on the game board.

    Args:
        map: The current game board.
"""
def get_possible_moves(map):
    moves = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                moves.append((x, y))
    return moves

"""
    Implements the minimax algorithm with alpha-beta pruning.

    Args:
        map: The current game board.
        depth: The depth of the search tree.
        alpha: The alpha value for pruning.
        beta: The beta value for pruning.
        maximazingPlayer: Boolean indicating whether it is maximizing or minimizing.
        player: The current player.
        opponent: The opponent player.
"""
def minimax(map, depth, alpha, beta, maximazingPlayer, player, opponent):
    if depth == 0:
        return heuristic_computation(map, player, opponent), None
    moves = get_possible_moves(map)
    if maximazingPlayer:
        max_score = float('-inf')
        best_move = None
        for move in moves:
            x, y = move
            map[y][x] = player
            score, _ = minimax(map, depth - 1, alpha, beta, False, player, opponent)
            map[y][x] = 0
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score, best_move
    else:
        min_score = float('inf')
        best_move = None
        for move in moves:
            x, y = move
            map[y][x] = opponent
            score, _ = minimax(map, depth - 1, alpha, beta, True, player, opponent)
            map[y][x] = 0
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score, best_move

"""
    Call the ai algorithm

"""
def ai_algorithm(map, size):
    player = 1
    opponent = 2 
    depth = 2
    copy_map = copy.deepcopy(map)
    best_score, best_move = minimax(copy_map, depth, float('-inf'), float('inf'), True, player, opponent)
    return best_move
