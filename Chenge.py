
class ChangeHand:

    def receive_my_hand(self, drawcards, card_decks, num1, num2, num3):

        # 手札格納
        my_hand = []
        for i in drawcards:
            my_hand.append(i)

        self.my_hand = my_hand
        # 手札表示
        print('手札表示')
        print(self.my_hand)
        print('-------------------------------')

        # デッキ格納
        deck_list = []
        for i in card_decks:
            deck_list.append(i)

        self.deck_list = deck_list

        # 残りのデッキ一覧表示
        print('残りデッキ一覧')
        print(self.deck_list)
        print('-------------------------------')

        # 交換1
        self.my_hand.pop(num1-1)
        self.my_hand.append(self.deck_list.pop(0))

        # 交換２
        if num2 != None:
            self.my_hand.pop(num2-2)
            self.my_hand.append(self.deck_list.pop(0))

        # 交換３
        if num3 != None:
            self.my_hand.pop(num3-3)
            self.my_hand.append(self.deck_list.pop(0))

        # 手札最終表示
        print('交換済み手札表示')
        print(self.my_hand)
        return self.my_hand


if __name__ == '__main__':

    mh = ChangeHand()
    #mh.receive_my_hand([1,2,3,4,5],[6,7,8,9] , 2 ,None,None)
    #mh.receive_my_hand([1,2,3,4,5],[6,7,8,9] , 2 ,3,None)

    #実際に渡される配列を想定して引数を渡してみる

    #club Q, heart Q, heart A, spade Q, diamond Q
    check_1 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 0, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    #club J, club K, club A, daimond J, diamond K
    check_2 = [{'number': 4, 'symbol': 'Clubs', 'string': 'ClubsJ'}, {'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 1, 'symbol': 'Clubs', 'string': 'ClubsA'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}, {'number': 2, 'symbol': 'Diamonds', 'string': 'DiamondsK'}]
    #mh.receive_my_hand(check_1, check_2, 2, 3, 4)
    mh.receive_my_hand(check_1, check_2, 1, 5, None)

