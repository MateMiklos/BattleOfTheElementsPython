from random import randint

import classes
import builder
import abilities
import logger
import autoplay


def game():
    game = initialiseNewGame()
    while game.getPlayer1().getLifeTotal() > 0 and game.getPlayer2().getLifeTotal() > 0:
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
    setManaToZero(player)
    dealBoard(player.getDeck())


def setManaToZero(player):
    if player.getManaTotal() < 0:
        player.setManaTotal(0)


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
        except TypeError:
            drawPile = []
    if len(deal) < deck.getDealSize():
        for i in range(deck.getDealSize() - len(deal)):
            deal.append(builder.buildFatigue(i + 1))
    deck.setDeal(deal)
    deck.setDrawPile(drawPile)
    if len(drawPile) == 0:
        reshuffle(deck)


def reshuffle(deck):
    drawPile = deck.getDrawPile()
    discardPile = deck.getDiscardPile()
    for card in discardPile:
        drawPile.append(card)
    discardPile = []
    deck.setDrawPile(drawPile)
    deck.setDiscardPile(discardPile)


def mainPhase(activePlayer, passivePlayer, game):
    cantBeSelectedCards = []
    playerInput = getPlayerInput()
    selectedCard = selectCardFromDeal(activePlayer, playerInput, cantBeSelectedCards)
    castSelectedCard(selectedCard, activePlayer, passivePlayer, game)
    sufferFatigueDamage(activePlayer)
    discardUnselectedCards(activePlayer.getDeck())


def getPlayerInput():
    randomInput = autoplay.getRandomInput()
    return randomInput  # TODO: set player input


def selectCardFromDeal(activePlayer, playerInput, cantBeSelectedCards):
    deck = activePlayer.getDeck()
    deal = deck.getDeal()
    selectedCard = deal[playerInput - 1]
    if canBeSelected(selectedCard, activePlayer):
        deal.remove(selectedCard)
        deck.setDeal(deal)
        return selectedCard
    else:
        if selectedCard not in cantBeSelectedCards:
            cantBeSelectedCards.append(selectedCard)
        if len(cantBeSelectedCards) == activePlayer.getDeck().getDealSize():
            return builder.buildManaPotion()
        playerInput = getPlayerInput()
        return selectCardFromDeal(activePlayer, playerInput, cantBeSelectedCards)


def canBeSelected(card, player):
    if card.getName() == 'Fatigue':
        return False
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


def sufferFatigueDamage(activePlayer):
    damage = countFatigueDamage(activePlayer.getDeck().getDeal())
    lifeTotal = activePlayer.getLifeTotal() - damage
    activePlayer.setLifeTotal(lifeTotal)


def countFatigueDamage(deal):
    damageSum = 0
    fatigueDamage = 1
    for card in deal:
        if card.getName() == 'Fatigue':
            damageSum += fatigueDamage
            fatigueDamage += 1
    return damageSum


def discardUnselectedCards(deck):
    deal = deck.getDeal()
    discardPile = deck.getDiscardPile()
    for card in deal:
        if card.getName() != 'Fatigue':
            discardPile.append(card)
            print(card.getName())
    deal = []
    deck.setDeal(deal)
    deck.setDiscardPile(discardPile)


def endPhase(game):
    activePlayer = decleareActivePlayer(game)
    passivePlayer = declearePassivePlayer(game)
    activePlayer.setActive(False)
    passivePlayer.setActive(True)
    logger.logInfo(game, activePlayer)


game()
