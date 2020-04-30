import classes
import builder


def game():
    game = initialiseNewGame()
    print(game.getPlayer1().getLifeTotal())
    return 0


def initialiseNewGame():
    classes.Deck(builder.buildBasicDeck())
    player1 = classes.Player('Peter', classes.Deck(builder.buildBasicDeck()))
    player2 = classes.Player('Matt', classes.Deck(builder.buildBasicDeck()))
    game = classes.Game(player1, player2)
    return game


def turn():
    return 0


game()
