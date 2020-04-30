import classes


# ===== BUILD CARDS ===== #


def buildFireball():
    name = 'Fireball'
    manacost = 4
    elementType = 'Fire'
    spellType = 'Instant'
    abilityDescription = 'Deals 6 Damage to your opponent.'
    return classes.Card(name, manacost, elementType, spellType, abilityDescription)


def buildSpring():
    name = 'Spring'
    manacost = 4
    elementType = 'Water'
    spellType = 'Instant'
    abilityDescription = 'Heals 6 Damage from you.'
    return classes.Card(name, manacost, elementType, spellType, abilityDescription)


def buildImmobilize():
    name = 'Immobilize'
    manacost = 2
    elementType = 'Earth'
    spellType = 'Instant'
    abilityDescription = 'Your opponent lose 4 mana.'
    return classes.Card(name, manacost, elementType, spellType, abilityDescription)


def buildSprint():
    name = 'Sprint'
    manacost = 2
    elementType = 'Air'
    spellType = 'Instant'
    abilityDescription = 'Your gain 4 mana.'
    return classes.Card(name, manacost, elementType, spellType, abilityDescription)


# ===== BUILD DECKS ===== #


def buildBasicDeck():
    deck = []
    for i in range(10):
        deck.append(buildFireball())
        deck.append(buildSpring())
        deck.append(buildImmobilize())
        deck.append(buildSprint())
    return deck
