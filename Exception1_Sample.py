""" Sample exception code within Python platform """

from random import randrange


class Game:

    def begin_game(self):
        number_val = randrange(100)
        while True:
            try:
                guess = int(input("Guess a number! "))
            except ValueError:
                continue
            if guess == number_val:
                print("You won the game")
                break


start_game = Game()
start_game.begin_game()
