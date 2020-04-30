import classes
import builder


def game():
    game = initialiseNewGame()
    print(game)
    return 0


def initialiseNewGame():
    player1 = classes.Player('Peter', classes.Deck(builder.buildBasicDeck()))
    player2 = classes.Player('Matt', classes.Deck(builder.buildBasicDeck()))
    game = classes.Game(player1, player2)
    return game


def turn():
    #beginnerPhase()
    #mainPhase()
    #endPhase()
    return 0


game()
