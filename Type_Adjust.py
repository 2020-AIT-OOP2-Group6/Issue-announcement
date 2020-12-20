def Adjust(card_stringlong):
    card_short = {'number': 1, 'symbol': 'none', 'string': 'none'}
    if 'Clubs' in card_stringlong:
        card_short['symbol'] = 'Clubs'
        if 'A' in card_stringlong:
            card_short['number'] = 1
            card_short['string'] = 'ClubsA'
        if 'K' in card_stringlong:
            card_short['number'] = 2
            card_short['string'] = 'ClubsK'
        if 'Q' in card_stringlong:
            card_short['number'] = 3
            card_short['string'] = 'ClubsQ'
        if 'J' in card_stringlong:
            card_short['number'] = 4
            card_short['string'] = 'ClubsJ'
    if 'Hearts' in card_stringlong:
        card_short['symbol'] = 'Hearts'
        if 'A' in card_stringlong:
            card_short['number'] = 1
            card_short['string'] = 'HeartsA'
        if 'K' in card_stringlong:
            card_short['number'] = 2
            card_short['string'] = 'HeartsK'
        if 'Q' in card_stringlong:
            card_short['number'] = 3
            card_short['string'] = 'HeartsQ'
        if 'J' in card_stringlong:
            card_short['number'] = 4
            card_short['string'] = 'HeartsJ'
    if 'Spades' in card_stringlong:
        card_short['symbol'] = 'Spades'
        if 'A' in card_stringlong:
            card_short['number'] = 1
            card_short['string'] = 'SpadesA'
        if 'K' in card_stringlong:
            card_short['number'] = 2
            card_short['string'] = 'SpadesK'
        if 'Q' in card_stringlong:
            card_short['number'] = 3
            card_short['string'] = 'SpadesQ'
        if 'J' in card_stringlong:
            card_short['number'] = 4
            card_short['string'] = 'SpadesJ'
    if 'Diamonds' in card_stringlong:
        card_short['symbol'] = 'Diamonds'
        if 'A' in card_stringlong:
            card_short['number'] = 1
            card_short['string'] = 'DiamondsA'
        if 'K' in card_stringlong:
            card_short['number'] = 2
            card_short['string'] = 'DiamondsK'
        if 'Q' in card_stringlong:
            card_short['number'] = 3
            card_short['string'] = 'DiamondsQ'
        if 'J' in card_stringlong:
            card_short['number'] = 4
            card_short['string'] = 'DiamondsJ'
    return card_short
