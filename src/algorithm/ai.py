import time

def evaluate_position(map_data, x, y, player):
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 0
        for step in range(-4, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]):
                if map_data[ny][nx] == player:
                    count += 1
                elif map_data[ny][nx] != 0:
                    count = 0
                    break
        score = max(score, count)
    return score

def get_possible_moves(map_data):
    """
    Returns a list of all possible moves (empty cells) on the board.
    """
    moves = []
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == 0:
                moves.append((x, y))
    return moves

def ai_algorithm(map_data, time_limit=5, depth=1):
    start_time = time.time()
    best_score = -float('inf')
    best_move = None
    player = 2

    moves = get_possible_moves(map_data)

    for move in moves:
        x, y = move
        map_data[y][x] = player
        score = evaluate_position(map_data, x, y, player)
        
        if depth > 1:
            opponent = 1
            opponent_moves = get_possible_moves(map_data)
            for opp_move in opponent_moves:
                ox, oy = opp_move
                map_data[oy][ox] = opponent
                score -= evaluate_position(map_data, ox, oy, opponent)
                map_data[oy][ox] = 0

        map_data[y][x] = 0
        if score > best_score:
            best_score = score
            best_move = move
        if time.time() - start_time > time_limit:
            break

    return best_move
