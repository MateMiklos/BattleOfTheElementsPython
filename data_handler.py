import engine


def create_json_data(game_object):
    data = {'game': {
                'turn': game_object.getTurn(),
                'player1': {
                    'name': game_object.getPlayer1().getName(),
                    'active': game_object.getPlayer1().isActive(),
                    'lifeTotal': game_object.getPlayer1().getLifeTotal(),
                    'manaTotal': game_object.getPlayer1().getManaTotal(),
                    'deck': {
                        'drawPile': fill_cards_with_converted_cards(game_object.getPlayer1().getDeck().getDrawPile()),
                        'deal': fill_cards_with_converted_cards(game_object.getPlayer1().getDeck().getDeal()),
                        'ongoings': fill_cards_with_converted_cards(game_object.getPlayer1().getDeck().getOngoings()),
                        'discardPile':
                            fill_cards_with_converted_cards(game_object.getPlayer1().getDeck().getDiscardPile()),
                        'destroyedPile':
                            fill_cards_with_converted_cards(game_object.getPlayer1().getDeck().getDestroyedPile()),
                        'dealSize': game_object.getPlayer1().getDeck().getDealSize(),
                        'ongoingsSize': game_object.getPlayer1().getDeck().getOngoingsSize()
                        }
                    },
                'player2': {
                    'name': game_object.getPlayer2().getName(),
                    'active': game_object.getPlayer2().isActive(),
                    'lifeTotal': game_object.getPlayer2().getLifeTotal(),
                    'manaTotal': game_object.getPlayer2().getManaTotal(),
                    'deck': {
                        'drawPile': fill_cards_with_converted_cards(game_object.getPlayer2().getDeck().getDrawPile()),
                        'deal': fill_cards_with_converted_cards(game_object.getPlayer2().getDeck().getDeal()),
                        'ongoings': fill_cards_with_converted_cards(game_object.getPlayer2().getDeck().getOngoings()),
                        'discardPile':
                            fill_cards_with_converted_cards(game_object.getPlayer2().getDeck().getDiscardPile()),
                        'destroyedPile':
                            fill_cards_with_converted_cards(game_object.getPlayer2().getDeck().getDestroyedPile()),
                        'dealSize': game_object.getPlayer2().getDeck().getDealSize(),
                        'ongoingsSize': game_object.getPlayer2().getDeck().getOngoingsSize()
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
