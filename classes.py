# ===== CARD CLASS ===== #


class Card:

    def __init__(self, name, manacost, elementType, spellType, abilityDescription):
        self.__name = name
        self.__manacost = manacost
        self.__elementType = elementType
        self.__spellType = spellType
        self.__abilityDescription = abilityDescription

    def getName(self):
        return self.__name

    def getManacost(self):
        return self.__manacost

    def getElementType(self):
        return self.__elementType

    def getSpellType(self):
        return self.__spellType

    def getAbilityDescription(self):
        return self.__abilityDescription


# ===== DECK CLASS ===== #


class Deck:

    def __init__(self):
        self.__drawPile = []
        self.__deal = []
        self.__dealSize = 4
        self.__ongoings = []
        self.__ongoingsSize = 4
        self.__discardPile = []
        self.__destroyedPile = []


# ===== PLAYER CLASS ===== #


class Player:

    def __init__(self, name, deck):
        self.__name = name
        self.__deck = deck
        self.__lifeTotal = 30
        self.__manaTotal = 30

    def getDeck(self):
        return self.__deck

    def getName(self):
        return self.__name

    def getLifeTotal(self):
        return self.__lifeTotal

    def getManaTotal(self):
        return self.__manaTotal

    def setName(self, name):
        self.__name = name

    def setLifeTotal(self, lifeTotal):
        self.__lifeTotal = lifeTotal

    def setManaTotal(self, manaTotal):
        self.__manaTotal = manaTotal


# ===== PLAYER CLASS ===== #


class Game:

    def __init__(self, players):
        self.__turn = 0
        self.__player1 = players[0]
        self.__player2 = players[1]

    def getTurn(self):
        return self.__turn

    def getPlayer1(self):
        return self.__player1

    def getPlayer2(self):
        return self.__player2
