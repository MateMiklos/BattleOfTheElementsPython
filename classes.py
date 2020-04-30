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

    def __init__(self, deck):
        self.__drawPile = deck
        self.__deal = []
        self.__dealSize = 4
        self.__ongoings = []
        self.__ongoingsSize = 4
        self.__discardPile = []
        self.__destroyedPile = []

        def getDrawPile(self):
            return self.__drawPile

        def getDeal(self):
            return self.__deal

        def getDealSize(self):
            return self.__dealSize

        def getOngoings(self):
            return self.__ongoings

        def getOngoingsSize(self):
            return self.__ongoingsSize

        def getDiscardPile(self):
            return self.__discardPile

        def getDestroyedPile(self):
            return self.__destroyedPile

        def setDrawPile(self, drawPile):
            self.__drawPile = drawPile

        def setDeal(self, deal):
            self.__deal = deal

        def setDealSize(self, dealSize):
            self.__dealSize = dealSize

        def setOngoings(self, ongoings):
            self.__ongoings = ongoings

        def setOngoingsSize(self, ongoingsSize):
            self.__ongoingsSize = ongoingsSize

        def setDiscardPile(self, discardPile):
            self.__discardPile = discardPile

        def setDestroyedPile(self, destroyedPile):
            self.__destroyedPile = destroyedPile


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


# ===== GAME CLASS ===== #


class Game:

    def __init__(self, player1, player2):
        self.__turn = 0
        self.__player1 = player1
        self.__player2 = player2

    def getTurn(self):
        return self.__turn

    def getPlayer1(self):
        return self.__player1

    def getPlayer2(self):
        return self.__player2
