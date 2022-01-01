#!/usr/bin/env python3


from typing import List, NoReturn


def get_input():
    with open("./input.txt", "r") as f:
        return f.read().splitlines()


def is_bingo(board):
    BINGO = ["x", "x", "x", "x", "x"]
    for i in range(5):
        # Check columns
        if [
            board[i],
            board[i + 5],
            board[i + 10],
            board[i + 15],
            board[i + 20],
        ] == BINGO:
            return True

        # Check rows
        if [
            board[i * 5],
            board[i * 5 + 1],
            board[i * 5 + 2],
            board[i * 5 + 3],
            board[i * 5 + 4],
        ] == BINGO:
            return True
    return False


def mark(board: List[str], number: str) -> None:
    try:
        i = board.index(number)
        board[i] = "x"
    except ValueError as e:
        pass


def get_boards(lines) -> List[str]:
    boards = []
    current_board = []
    for i in range(len(lines)):
        if i != 0 and i % 6 == 0:
            boards.append(current_board)
            current_board = []
        else:
            current_board += lines[i].split()
    boards.append(current_board)
    return boards


def a():
    lines = get_input()
    chosen = lines[0].split(",")
    boards = get_boards(lines[1:])

    winner = None
    winner_number = None
    for n in chosen:
        for board in boards:
            mark(board, n)
            if is_bingo(board) is True:
                winner = board
                break
        if winner:
            winner_number = n
            break
    # print("winner:")
    # print(winner)

    sum_ = sum(int(s) for s in winner if s != "x")
    print(sum_ * int(winner_number))


def b():
    lines = get_input()
    chosen = lines[0].split(",")
    boards = get_boards(lines[1:])

    winner = None
    winner_number = None
    won = [False for board in boards]
    for n in chosen:
        for i, board in enumerate(boards):
            if won[i]:
                continue
            mark(board, n)
            if is_bingo(board):
                # print(f"{i} won")
                winner = board
                winner_number = n
                won[i] = True
        if all(won):
            # print(f"quit at {n} because all won")
            break

    # print("winner:")
    # print(winner)

    sum_ = sum(int(s) for s in winner if s != "x")
    print(sum_ * int(winner_number))


if __name__ == "__main__":
    a()
    b()
