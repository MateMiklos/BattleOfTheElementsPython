from random import randint

import classes
import builder


def game():
    game = initialiseNewGame()
    turn(game)
    return game


def initialiseNewGame():
    player1 = classes.Player('Peter', classes.Deck(builder.buildBasicDeck()))
    player2 = classes.Player('Matt', classes.Deck(builder.buildBasicDeck()))
    game = classes.Game(player1, player2)
    selectStarterPlayer(game)
    return game


def selectStarterPlayer(game):
    players = [game.getPlayer1(), game.getPlayer2()]
    starterPlayer = players[randint(0, 1)]
    starterPlayer.setActive(True)


def turn(game):
    increaseTurn(game)
    activePlayer = decleareActivePlayer(game)
    beginnerPhase(activePlayer)
    #mainPhase()
    #endPhase()


def increaseTurn(game):
    turn = game.getTurn()
    turn += 1
    game.setTurn(turn)


def decleareActivePlayer(game):
    if game.getPlayer1().isActive():
        return game.getPlayer1()
    elif game.getPlayer2().isActive():
        return game.getPlayer2()


def beginnerPhase(player):
    #removeTimeCounters(palyer.getDeck())
    dealBoard(player.getDeck())


def dealBoard(deck):
    drawPile = deck.getDrawPile()
    deal = []
    for i in range(deck.getDealSize()):
        try:
            randIndex = randint(0, len(deck.getDrawPile()) - 1)
            deal.append(drawPile[randIndex])
            drawPile.remove(drawPile[randIndex])
        except ValueError:
            for card in drawPile:
                deal.append(card)
                drawPile.remove(card)
    deck.setDrawPile(drawPile)
    deck.setDeal(deal)


game()
