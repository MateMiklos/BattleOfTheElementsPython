def logInfo(game, activePlayer):
    name = activePlayer.getName()
    castedCard = activePlayer.getDeck().getDestroyedPile()[-1].getName()
    try:
        print(
            '******************************************' + '\n' +
            'It\'s turn ' + str(game.getTurn()) + '\n' +
            '==========================================' + '\n' +
            name + ' has casted ' + castedCard + '\n' +
            '==========================================' + '\n' +
            game.getPlayer1().getName() + '\'s lifetotal: ' + str(game.getPlayer1().getLifeTotal()) + '\n' +
            game.getPlayer1().getName() + '\'s manatotal: ' + str(game.getPlayer1().getManaTotal()) + '\n' +
            '==========================================' + '\n' +
            game.getPlayer1().getName() + '\'s drawpile: ' + str(len(game.getPlayer1().getDeck().getDrawPile())) + '\n'
            + game.getPlayer1().getName() + '\'s discarpile: ' + str(len(game.getPlayer1().getDeck().getDiscardPile()))
            + '\n' + '==========================================' + '\n' +
            game.getPlayer2().getName() + '\'s lifetotal: ' + str(game.getPlayer2().getLifeTotal()) + '\n' +
            game.getPlayer2().getName() + '\'s manatotal: ' + str(game.getPlayer2().getManaTotal()) + '\n' +
            '==========================================' + '\n' +
            game.getPlayer2().getName() + '\'s drawpile: ' + str(len(game.getPlayer2().getDeck().getDrawPile())) + '\n'
            + game.getPlayer2().getName() + '\'s discarpile: ' + str(len(game.getPlayer2().getDeck().getDiscardPile()))
            + '\n' + '******************************************' + '\n'
            )
    except TypeError:
        print(
            '******************************************' + '\n' +
            'It\'s turn ' + str(game.getTurn()) + '\n' +
            '==========================================' + '\n' +
            name + ' has casted ' + castedCard + '\n' +
            '==========================================' + '\n' +
            game.getPlayer1().getName() + '\'s lifetotal: ' + str(game.getPlayer1().getLifeTotal()) + '\n' +
            game.getPlayer1().getName() + '\'s manatotal: ' + str(game.getPlayer1().getManaTotal()) + '\n' +
            '==========================================' + '\n' +
            game.getPlayer1().getName() + '\'s drawpile: 0' + '\n' +
            game.getPlayer1().getName() + '\'s discarpile: 0' + '\n'
            + '==========================================' + '\n' +
            game.getPlayer2().getName() + '\'s lifetotal: ' + str(game.getPlayer2().getLifeTotal()) + '\n' +
            game.getPlayer2().getName() + '\'s manatotal: ' + str(game.getPlayer2().getManaTotal()) + '\n' +
            '==========================================' + '\n' +
            game.getPlayer2().getName() + '\'s drawpile: 0' '\n' +
            game.getPlayer2().getName() + '\'s discarpile: 0' + '\n'
            + '******************************************' + '\n'
            )
