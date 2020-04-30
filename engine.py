from random import randint

import classes
import builder
import abilities


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
    passivePlayer = declearePassivePlayer(game)
    beginnerPhase(activePlayer)
    mainPhase(activePlayer, passivePlayer, game)
    endPhase(game)


def increaseTurn(game):
    turn = game.getTurn()
    turn += 1
    game.setTurn(turn)


def decleareActivePlayer(game):
    if game.getPlayer1().isActive():
        return game.getPlayer1()
    elif game.getPlayer2().isActive():
        return game.getPlayer2()


def declearePassivePlayer(game):
    if game.getPlayer1().isActive() is False:
        return game.getPlayer1()
    elif game.getPlayer2().isActive() is False:
        return game.getPlayer2()


def beginnerPhase(player):
    # removeTimeCounters(palyer.getDeck())
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


def mainPhase(activePlayer, passivePlayer, game):
    playerInput = getPlayerInput()
    selectedCard = selectCardFromDeal(activePlayer, playerInput)
    castSelectedCard(selectedCard, activePlayer, passivePlayer, game)
    discardUnselectedCards(activePlayer.getDeck())


def getPlayerInput():
    return 1  # TODO: set player input


def selectCardFromDeal(activePlayer, playerInput):
    deck = activePlayer.getDeck()
    deal = deck.getDeal()
    selectedCard = deal[playerInput - 1]
    if canBeSelected(selectedCard, activePlayer):
        deal.remove(selectedCard)
        deck.setDeal(deal)
        return selectedCard
    selectCardFromDeal(activePlayer, getPlayerInput())


def canBeSelected(card, player):
    if card.getManacost() <= player.getManaTotal():
        return True
    return False


def castSelectedCard(card, activePlayer, passivePlayer, game):
    castSelectedCardAbility(card, activePlayer, passivePlayer)
    deck = activePlayer.getDeck()
    destroyedPile = deck.getDestroyedPile()
    destroyedPile.append(card)
    deck.setDestroyedPile(destroyedPile)


def castSelectedCardAbility(card, activePlayer, passivePlayer):
    abilityToCast = getattr(abilities, card.getName().lower())
    abilityToCast(activePlayer, passivePlayer)


def discardUnselectedCards(deck):
    deal = deck.getDeal()
    discardPile = deck.getDiscardPile()
    for card in deal:
        discardPile.append(card)
    deal = []
    deck.setDeal(deal)
    deck.setDiscardPile(discardPile)


def endPhase(game):
    activePlayer = decleareActivePlayer(game)
    passivePlayer = declearePassivePlayer(game)
    activePlayer.setActive(False)
    passivePlayer.setActive(True)


game()
