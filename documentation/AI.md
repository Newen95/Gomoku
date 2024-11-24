Documentation for Gomoku AI Implementation
===
## Overview:

This AI is designed to make intelligent moves in the Gomoku game by evaluating the game board and predicting potential outcomes using a minimax algorithm with alpha-beta pruning. The AI incorporates a heuristic scoring function to analyze the board state and determine optimal moves.

## How It Works:

    Heuristic Evaluation:
        The AI uses heuristic functions to evaluate the board based on current and future alignment opportunities for both players.

    Minimax with Alpha-Beta Pruning:
        The minimax algorithm recursively evaluates moves to a certain depth, predicting potential future board states.
        Alpha-beta pruning improves efficiency by eliminating nodes that won't influence the final decision.