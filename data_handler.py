import engine


def create_json_data():
    game = engine.initialiseNewGame()
    data = {'game': {
                'turn': game.turn,
                'player1': {
                    'name': game.player1.getName(),
                    'lifeTotal': game.player1.getLifeTotal(),
                    'manaTotal': game.player1.getManaTotal(),
                    'deck': {
                        'cards': fill_cards_with_converted_cards(game.player1.getDeck().cards),
                        'board': fill_cards_with_converted_cards(game.player1.getDeck().board),
                        'ongoings': fill_cards_with_converted_cards(game.player1.getDeck().ongoings),
                        'discardPile': fill_cards_with_converted_cards(game.player1.getDeck().discardPile),
                        'boardSize': game.player1.getDeck().boardSize,
                        'ongoingsSize': game.player1.getDeck().ongoingsSize
                        }
                    },
                'player2': {
                    'name': game.player2.getName(),
                    'lifeTotal': game.player2.getLifeTotal(),
                    'manaTotal': game.player2.getManaTotal(),
                    'deck': {
                        'cards': fill_cards_with_converted_cards(game.player2.getDeck().cards),
                        'board': fill_cards_with_converted_cards(game.player2.getDeck().board),
                        'ongoings': fill_cards_with_converted_cards(game.player2.getDeck().ongoings),
                        'discardPile': fill_cards_with_converted_cards(game.player2.getDeck().discardPile),
                        'boardSize': game.player1.getDeck().boardSize,
                        'ongoingsSize': game.player1.getDeck().ongoingsSize
                        }
                    }
                }
            }
    return data


def convert_cards(card):
    converted_card = {
        'name': card.getName(),
        'manacost': card.getManacost(),
        'elementType': card.getElementType(),
        'spellType': card.getSpellType(),
        'abilityDescription': card.getAbilityDescription()
    }
    return converted_card


def fill_cards_with_converted_cards(card_list):
    converted_card_list = []
    for card in card_list:
        converted_card_list.append(convert_cards(card))
    return converted_card_list
