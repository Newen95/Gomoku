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

def heuristic_computation(board, player, opponent):
    score = 0

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == player:
                score += win_score(board, x, y, player, opponent)
            elif board[y][x] == opponent:
                score -= 2 * win_score(board, x, y, opponent, player)
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
def win_score(board, x, y, player, opponent):
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        multiplier = 1.0
        if (dx, dy) in [(1, 1), (1, -1)]:
            multiplier = 1.5
        
        player_count = 0
        blocks = 0
        open_start = False
        open_end = False

        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                cell = board[ny][nx]
                if cell == player:
                    player_count += 1
                elif cell == opponent:
                    blocks += 1
                elif cell == 0:
                    if step == -4:
                        open_start = True
                    if step == 4:
                        open_end = True
            else:
                blocks += 1

        if player_count >= 5:
            score += int(10000 * multiplier)
        elif player_count == 4:
            if open_start or open_end:
                score += int(800 * multiplier)
            else:
                score += int(500 * multiplier)
        elif player_count == 3:
            if open_start and open_end:
                score += int(150 * multiplier)
            else:
                score += int(40 * multiplier)
        elif player_count == 2:
            if open_start and open_end:
                score += int(20 * multiplier)
            elif open_start or open_end:
                score += int(10 * multiplier)
        elif player_count == 1:
            score += int(1 * multiplier)
    return score


"""
    Retrieves all possible moves on the game board.

    Args:
        map: The current game board.
"""
def get_possible_moves(board):
    moves = []
    board_size = len(board)
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == 0:
                neighbor_found = False
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < board_size and 0 <= nx < board_size:
                            if board[ny][nx] != 0:
                                neighbor_found = True
                                break
                    if neighbor_found:
                        break
                if neighbor_found:
                    moves.append((x, y))
    if not moves:
        for y in range(board_size):
            for x in range(board_size):
                if board[y][x] == 0:
                    moves.append((x, y))
    center = board_size // 2
    moves.sort(key=lambda move: abs(move[0] - center) + abs(move[1] - center))
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
