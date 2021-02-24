#  filename: main.py
#  author: avivy
#  date created: 2020-11-22 9:07 p.m.
#  last modified: 2020-11-22

import random
import sys
import copy
import numpy as np


class Game:
    "Tic-Tac-Toe class. This class holds the user interaction, and game logic"

    def __init__(self):
        self.board = [' '] * 9
        self.player_name = ''
        self.player_marker = ''
        self.bot_name = 'Player 2'
        self.bot_marker = ''
        self.winning_combos = (
            [6, 7, 8],
            [3, 4, 5],
            [0, 1, 2],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        )
        self.corners = [0, 2, 6, 8]
        self.sides = [1, 3, 5, 7]
        self.middle = 4

        self.form = '''
			\t| %s | %s | %s |
			\t-------------
			\t| %s | %s | %s |
			\t-------------
			\t| %s | %s | %s |
           	'''

    def print_board(self, board=None):
        "Display board on screen"
        if board is None:
            print(self.form %
				tuple(self.board[0:3] + self.board[3:6] + self.board[6:9]))
        else:
            # when the game starts, display numbers on all the grids
        	print(self.form % tuple(board[0:3] +  board[3:6] + board[6:9]))
    def get_marker(self):

        marker = "X"
        while marker not in ["X", "Y"]:
            marker = input(
                "Would you like your marker to be X  or Y? :").upper()
        if marker == "X":
            return ('X', 'Y')
        else:
            return ('Y', 'X')

        def help(self):
            print("""
    \n\t The game board has 9 sqaures(3X3).
    \n\t Two players take turns in marking the spots/grids on the board.
    \n\t The first player to have 3 pieces in a horizontal, vertical or diagonal row wins the game.
    \n\t To place your mark in the desired square, simply type the number corresponding with the square on the grid

    \n\t Press Ctrl + C to quit""")

    def quit_game(self):
        "exits game"
        self.print_board
        print("\n\t Thanks for playing :-) \n\t Come play again soon!\n")
        sys.exit()

    def is_winner(self, board, marker, predict=False):
        "check if this marker will win the game"
        # order of checks:
        #   1. across the horizontal top
        #   2. across the horizontal middle
        #   3. across the horizontal bottom
        #   4. across the vertical left
        #   5. across the vertical middle
        #   6. across the vertical right
        #   7. across first diagonal
        #   8. across second diagonal
        for combo in self.winning_combos:

            # if set(combo) == marker:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] ==
                    marker):
                return True
        return False

    def is_space_free(self, board, index):
        "checks for free space of the board"
        # print "SPACE %s is taken" % index
        return board[index] == ' '
        
        
    def is_board_full(self):
        
        "checks if the board is full"
        for i in range(1, 9):
            if self.is_space_free(self.board, i):
                return False
        return True

    def make_move(self, board, index, move):
        board[index] = move

    def choose_random_move(self):
        get_move = lambda: random.randint(1, 9)
        move = get_move()
        while not self.is_space_free(self.board, move - 1):
            # move = int(input("Invalid move. Please try again: (1-9)"))
            move = get_move()
        return move - 1

    def basic_strat(self, board, move, marker):
        for i, j in zip(self.sides, self.corners):
            if marker == board[i] and marker == board[j]:
                return True
        if self.is_space_free(board, [i for i in corners]):

             return True
        good_move = combo >> 1
        good_move = {good_move[:1]}
        if len(good_move) == 2:
            return True


    def smart_move(self):
		"""looks at all possible next moves with a depth of (Insert number), [not known yet how far this will go], and plays moves that do not result in a loss"""

    possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        is_exist = lambda x: x in possibles

        future_board = self.board
        getm = lambda x=possibles: random.choice(x)

        check_space = lambda m, b=future_board: self.is_space_free(b, m - 1)

        move = getm()
        # move = getm()
        exp_move = getm()
        while not check_space(move, self.board):
            move = getm()
        self.make_move(future_board, move - 1, self.bot_marker)
        future_board = self.board
        while not check_space(exp_move):
            exp_move = getm()

        if not self.is_winner(future_board, self.player_marker):
            move = getm()
            self.make_move(future_board, move - 1, self.player_marker)
            future_board = self.board
        # return move - 1  # not working
        return getm() # random for now

    def get_player_move(self):
        move = int(input("Pick a spot to move: (1-9) "))
        while move not in [i for i in range(1,10)] or not self.is_space_free(self.board, move - 1):
            move = int(input("Invalid move. Please try again: (1-9) "))
        return move - 1

    def toggle(self, marker):

        if marker == "h":
            marker = "b"
        elif marker == "b":
            marker = "h"
        return marker

    def incr_score(self, name):
        global scores
        scores[name] += 1

    def get_player_name(self):
        return input("Hi, i am %s" % self.bot_name + ". What is your name? ")
        return "Player 1"

    def start_game(self):
        "welcomes user, prints help message and hands over to the main game loop"
        # welcome user
        print("""Game
//-----------------------//""")
        self.print_board([i for i in range(1, 10)])
        self.player_name = self.get_player_name()

        # get user's preferred marker
        self.player_marker, self.bot_marker = self.get_marker()
        print("Your marker is " + self.player_marker)

        # randomly decide who can play first
        if random.randint(0, 1) == 0:
            print("I will go first")
            # self.make_move(self.board, random.choice(self.corners),
            #                self.bot_marker)
            self.print_board()
            self.game('b')
        else:
            print("You will go first")
            # now, enter the main game loop
            self.game('h')

    def check_end(self):
        if self.is_board_full():
            print("\nDraw")
            return True
            # break
        return False

    def game(self, turn):
        "starts the main game loop"
        is_running = True
        player = turn  # h for human, b for bot
        while is_running:
            self.print_board()
            if player == "h":
                user_input = self.get_player_move()
                self.make_move(self.board, user_input, self.player_marker)
                if (self.is_winner(self.board, self.player_marker)):
                    self.print_board()
                    print("\nWinner: %s" % (self.player_name))
                    self.incr_score("p1")
                    is_running = False
                else:
                    if self.check_end():
                        self.print_board()
                        is_running = False
                    else:
                        self.print_board()
                        player = "b"
            # bot's turn to play
            elif player == "b":
                self.make_move(self.board, self.smart_move(), self.bot_marker)
                if (self.is_winner(self.board, self.bot_marker)):
                    self.print_board()
                    print("\nWinner: %s" % self.bot_name)
                    self.incr_score("p2")
                    is_running = False
                else:
                    if self.check_end():
                        self.print_board()
                        is_running = False

                    else:
                        self.print_board()
                        player = "h"


scores = {"p1": 0, "p2": 0}


def run_game():
    tictac = Game()
    # for j in range(10):
    # print(i*j)
    tictac.start_game()


for i in range(1):

    run_game()
print(scores, "4")
