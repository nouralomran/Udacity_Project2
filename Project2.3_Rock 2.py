#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
userScore = 0
computerScore = 0
moves = ['rock', 'paper', 'scissors']
Player_Type = ['rocker', 'reflect', 'cycle', 'random']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.enemy_last_move = 'paper'
        self.my_last_move = "rock"
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.enemy_last_move = their_move

# print the choices by reflect humanplayer choices


class ReflectPlayer(Player):

    def move(self):
        return self.enemy_last_move

# cycle player print the choices by cycle


class CyclePlayer(Player):

    def move(self):
        if self.my_last_move == "rock":
            return ("paper")
        elif self.my_last_move == "paper":
            return ("scissors")
        elif self.my_last_move == "scissors":
            return ("rock")

# random player choose the choices randomly


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        HumanPlayerMoves = ""
        while HumanPlayerMoves not in moves:
            HumanPlayerMoves = input(
                "What do you choose to play? Enter your choice: ").lower()
        return HumanPlayerMoves

# it shows weather first move beats second move


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # find out who is the winner in this round
        #  counting the score
        if beats(move1, move2):
            self.p1.score += 1
            print("You win this round")
            print(self.p1.score, self.p2.score)
            self.p1.score + 1
        elif beats(move2, move1):
            self.p2.score += 1
            print("You lose this round")
            print(self.p1.score, self.p2.score)
            self.p2.score + 1
        else:
            print("TIE")
            print(self.p1.score, self.p2.score)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        # show who won
        if self.p1.score > self.p2.score:
            print("You are the winner")
            print(self.p1.score, self.p2.score)
        elif self.p1.score < self.p2.score:
            print("You lose in this game!")
            print(self.p1.score, self.p2.score)
        else:
            print("TIE")
            print(self.p1.score, self.p2.score)


if __name__ == '__main__':
    # For spelling errors entered by user
    PlayerType = ""
    while PlayerType not in Player_Type:
        PlayerType = input("What do you pick to play against?" +
                           "(rocker, reflect, cycle, random): ").lower()

    if PlayerType == 'rocker':
        game = Game(HumanPlayer(), Player())
    elif PlayerType == 'reflect':
        game = Game(HumanPlayer(), ReflectPlayer())
    elif PlayerType == 'cycle':
        game = Game(HumanPlayer(), CyclePlayer())
    elif PlayerType == 'random':
        game = Game(HumanPlayer(), RandomPlayer())

    game.play_game()