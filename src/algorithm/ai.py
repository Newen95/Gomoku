## EPITECH PROJECT, 2024
## Gomoku
## File description:
## ai

import time
import copy
from typing import List, Tuple, Optional, Dict


class TranspositionTable:
    def __init__(self, max_size: int = 1000000):
        self.table: Dict[str, Tuple[int, float, Tuple[int, int], str]] = {}
        self.max_size = max_size

    def store(self, board_hash: str, depth: int, score: float, move: Tuple[int, int], flag: str):
        if len(self.table) >= self.max_size:
            self.table.clear()
        self.table[board_hash] = (depth, score, move, flag)

    def lookup(self, board_hash: str) -> Optional[Tuple[int, float, Tuple[int, int], str]]:
        return self.table.get(board_hash)


def board_to_hash(board: List[List[int]]) -> str:
    return ''.join(str(cell) for row in board for cell in row)


def detect_multiple_threats(board: List[List[int]], x: int, y: int, player: int) -> int:
    threats = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        open_threes = 0
        open_fours = 0
        for direction in [-1, 1]:
            count = 1
            spaces = 0
            nx, ny = x + dx * direction, y + dy * direction
            
            while 0 <= nx < len(board) and 0 <= ny < len(board) and spaces < 2:
                if board[ny][nx] == 0:
                    spaces += 1
                elif board[ny][nx] == player:
                    count += 1
                else:
                    break
                nx += dx * direction
                ny += dy * direction
            
            if count == 3 and spaces == 1:
                open_threes += 1
            elif count == 4 and spaces == 1:
                open_fours += 1
                
        if open_threes >= 2 or open_fours >= 1:
            threats += 1
            
    return threats


def check_immediate_win(board: List[List[int]], x: int, y: int, player: int) -> bool:
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        for direction in [-1, 1]:
            nx, ny = x, y
            while True:
                nx += dx * direction
                ny += dy * direction
                if not (0 <= nx < len(board) and 0 <= ny < len(board)):
                    break
                if board[ny][nx] != player:
                    break
                count += 1
        if count >= 5:
            return True
    return False


def evaluate_position(board: List[List[int]], x: int, y: int, player: int, opponent: int) -> float:
    patterns = {
        'five': 100000,
        'open_four': 15000,
        'four': 10000,
        'open_three': 3000,
        'three': 1000,
        'open_two': 200,
        'two': 100
    }
    
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        multiplier = 1.5 if (dx, dy) in [(1, 1), (1, -1)] else 1.0
        count = 1
        spaces = 0
        blocked = 0

        nx, ny = x + dx, y + dy
        while 0 <= nx < len(board) and 0 <= ny < len(board) and spaces < 2:
            if board[ny][nx] == 0:
                spaces += 1
            elif board[ny][nx] == player:
                count += 1
            else:
                blocked += 1
                break
            nx += dx
            ny += dy

        nx, ny = x - dx, y - dy
        spaces_back = 0
        while 0 <= nx < len(board) and 0 <= ny < len(board) and spaces_back < 2:
            if board[ny][nx] == 0:
                spaces_back += 1
            elif board[ny][nx] == player:
                count += 1
            else:
                blocked += 1
                break
            nx -= dx
            ny -= dy
            
        total_spaces = spaces + spaces_back
        
        if count >= 5:
            score += patterns['five'] * multiplier
        elif count == 4:
            if blocked == 0:
                score += patterns['open_four'] * multiplier
            else:
                score += patterns['four'] * multiplier
        elif count == 3:
            if blocked == 0 and total_spaces >= 2:
                score += patterns['open_three'] * multiplier
            else:
                score += patterns['three'] * multiplier
        elif count == 2:
            if blocked == 0 and total_spaces >= 3:
                score += patterns['open_two'] * multiplier
            else:
                score += patterns['two'] * multiplier

    threats = detect_multiple_threats(board, x, y, player)
    if threats >= 2:
        score += threats * 5000
        
    return score


def heuristic_computation(board: List[List[int]], player: int, opponent: int) -> float:
    score = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == player:
                score += evaluate_position(board, x, y, player, opponent)
            elif board[y][x] == opponent:
                score -= 2 * evaluate_position(board, x, y, opponent, player)
    return score


def get_possible_moves(board: List[List[int]]) -> List[Tuple[int, int]]:
    moves = []
    visited = set()
    board_size = len(board)

    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] != 0:
                for dy in range(-2, 3):
                    for dx in range(-2, 3):
                        ny, nx = y + dy, x + dx
                        if (0 <= ny < board_size and 
                            0 <= nx < board_size and 
                            board[ny][nx] == 0 and 
                            (nx, ny) not in visited):
                            moves.append((nx, ny))
                            visited.add((nx, ny))

    if not moves:
        center = board_size // 2
        for y in range(board_size):
            for x in range(board_size):
                if board[y][x] == 0:
                    moves.append((x, y))
        moves.sort(key=lambda move: abs(move[0] - center) + abs(move[1] - center))
        
    return moves


def minimax(board: List[List[int]], depth: int, alpha: float, beta: float, 
           maximizing_player: bool, player: int, opponent: int, 
           transposition_table: TranspositionTable, start_time: float, 
           max_time: float) -> Tuple[float, Optional[Tuple[int, int]]]:

    if time.time() - start_time > max_time:
        raise TimeoutError
        
    board_hash = board_to_hash(board)
    tt_entry = transposition_table.lookup(board_hash)
    
    if tt_entry is not None:
        stored_depth, stored_score, stored_move, _ = tt_entry
        if stored_depth >= depth:
            return stored_score, stored_move
            
    moves = get_possible_moves(board)
    
    if depth == 0:
        score = heuristic_computation(board, player, opponent)
        return score, None
        
    if maximizing_player:
        max_score = float('-inf')
        best_move = None
        
        for move in moves:
            x, y = move
            board[y][x] = player
            if check_immediate_win(board, x, y, player):
                board[y][x] = 0
                return 100000, move
                
            score, _ = minimax(board, depth - 1, alpha, beta, False, 
                             player, opponent, transposition_table, 
                             start_time, max_time)
            board[y][x] = 0
            
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, score)
            
            if beta <= alpha:
                break
                
        transposition_table.store(board_hash, depth, max_score, best_move, 'exact')
        return max_score, best_move
        
    else:
        min_score = float('inf')
        best_move = None
        
        for move in moves:
            x, y = move
            board[y][x] = opponent
            if check_immediate_win(board, x, y, opponent):
                board[y][x] = 0
                return -100000, move
                
            score, _ = minimax(board, depth - 1, alpha, beta, True, 
                             player, opponent, transposition_table, 
                             start_time, max_time)
            board[y][x] = 0
            
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, score)
            
            if beta <= alpha:
                break
                
        transposition_table.store(board_hash, depth, min_score, best_move, 'exact')
        return min_score, best_move


def ai_algorithm(map: List[List[int]], size: int) -> Tuple[int, int]:
    player = 1
    opponent = 2
    transposition_table = TranspositionTable()
    start_time = time.time()
    max_time = 4.5
    best_move = None
    
    try:
        for depth in range(1, 10):
            copy_map = copy.deepcopy(map)
            _, move = minimax(copy_map, depth, float('-inf'), float('inf'), 
                            True, player, opponent, transposition_table, 
                            start_time, max_time)
            if move is not None:
                best_move = move
                
    except TimeoutError:
        pass

    if best_move is None:
        moves = get_possible_moves(map)
        if moves:
            best_move = moves[0]
        else:
            center = size // 2
            best_move = (center, center)
            
    return best_move
