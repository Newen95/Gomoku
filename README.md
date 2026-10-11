# Gomoku AI

A Gomoku (five in a row) bot written in Python, built for the Epitech AI module.
It plays on a 20×20 board and talks to any game manager that implements the
[Gomocup / liskvork AI protocol](https://github.com/liskvork/docs/blob/master/src/ai_protocol_original.md),
such as [liskvork](https://github.com/liskvork/liskvork).

## How the AI plays

- **Minimax with alpha-beta pruning** explores the moves of both players and cuts
  branches that cannot change the decision.
- **Iterative deepening under a time budget**: the search goes one level deeper at a
  time and stops at 4.5 s, keeping the best move of the last completed depth, so the
  bot always answers within the protocol's time limit.
- **Transposition table**: already evaluated positions are cached to avoid searching
  them twice.
- **Candidate moves** are restricted to empty cells within two squares of an existing
  stone, which keeps the branching factor small on a 400-cell board.
- **Pattern heuristic**: each line is scored by shape (five, open four, four, open
  three…), diagonals weigh more, multiple simultaneous threats get a bonus, and the
  opponent's threats count double so the bot defends as much as it attacks.

More detail in [`documentation/Doc_AI.md`](documentation/Doc_AI.md).

## Protocol

Every protocol command lives in its own module under `src/command/`
(`START`, `TURN`, `BEGIN`, `BOARD`, `INFO`, `END`, `ABOUT`, `RESTART`,
`TAKEBACK`, `RECTSTART`), dispatched by `src/parse.py`; `src/algorithm/ai.py`
holds the search.

```
START 20      ->  OK
BEGIN         ->  10,10
TURN 11,11    ->  11,9
```

## Usage

Requires Python 3 and make.

```sh
make                 # builds the pbrain-gomoku-ai executable
./pbrain-gomoku-ai   # then speak the protocol on stdin/stdout, or plug it into liskvork
```

## Team

Built by a team of three:
[Sofiane Larbi](https://github.com/Sofiane-Larbi),
[Mélissa Mi You](https://github.com/melfrom987) and
[Newen Calle](https://github.com/Newen95).
