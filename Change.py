import random
import pandas as pd
import Compare

compare_class = Compare.CompareHand()


class ChangeHand:
    def make_card_list(self):
        # マークのリスト
        symbol_list = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        # カードリスト
        card_list = []

        # カードのデータを作成
        for symbol in symbol_list:
            for number in range(1, 5):
                card = {
                    'number': number,
                    'symbol': symbol
                }
                # マークと数字を合体させる
                # 11以上と1は置き換え
                if number == 1:
                    card['string'] = symbol + 'A'
                elif number == 2:
                    card['string'] = symbol + 'K'
                elif number == 3:
                    card['string'] = symbol + 'Q'
                elif number == 4:
                    card['string'] = symbol + 'J'

                # カードをリストに追加
                card_list.append(card)

        card_list.append({
            'number': 0,
            'symbol': 'Joker',
            'string': 'Joker'
        })
        self.card_list = card_list

    def deck_org(self, playerhand, comhand):
        self.d_str = [d.get('string') for d in self.card_list]
        self.p_str = [d.get('string') for d in playerhand]
        self.c_str = [d.get('string') for d in comhand]
        p_mutch_nlist = [self.d_str.index(d) for d in self.p_str]
        # 数字の昇順に並び替える
        p_mutch_nlist = sorted(p_mutch_nlist, reverse=True)
        for d in p_mutch_nlist:
            self.card_list.pop(d)
        self.d_str = [d.get('string') for d in self.card_list]
        c_mutch_nlist = [self.d_str.index(d) for d in self.c_str]
        # 数字の昇順に並び替える
        c_mutch_nlist = sorted(c_mutch_nlist, reverse=True)
        for d in c_mutch_nlist:
            self.card_list.pop(d)
        self.d_str = [d.get('string') for d in self.card_list]
        print(f'デッキ{self.d_str}')
        print(f'プレイヤーハンド{self.p_str}')
        print(f'COMハンド{self.c_str}')

    def comchange_select(self, comhand):
        # 数字の昇順に並び替える
        comhand = sorted(comhand, key=lambda x: x['number'])
        if comhand[0]['number'] == 0:
            # jokerアリの場合(com)
            c_point = compare_class.joker_handpoint(comhand)
        else:
            # joker無しの場合
            c_point = compare_class.handpoint(comhand)
        # print(c_point)

        if c_point < 400:  # ストレート以下なら交換（持っているカードのユニークを交換）
            # 最頻値を取り出す（ツーペアの場合二つ）
            mode_c_card = pd.DataFrame(comhand)['number'].mode().tolist()
            mode_c_card.sort()
            comhand = [x for x in comhand if not x['number'] == mode_c_card[0]]
            # print([d.get('string') for d in comhand])
            if not len(mode_c_card) == 1:
                # ツーペア
                # さらにユニークなもののみ
                comhand = [x for x in comhand if not x['number']
                           == mode_c_card[1]]
                # print([d.get('string') for d in comhand])
                return comhand

            if len(comhand) == 3:
                # ワンペアの場合（ユニークなカードの一枚目（強いカード）以外を交換）
                # JokerがあればJokerが残る（ワンペア＋Jokerのスリーカード）
                comhand.pop(0)
            # それ以外はユニークなものすべてを交換

            return comhand
        else:
            comhand = [None]
            return comhand

    def change_cards(self, playerhand, comhand, num1, num2, num3):
        self.make_card_list()
        self.deck_org(playerhand, comhand)

        # 数字の昇順に並び替える
        playerhand = sorted(playerhand, key=lambda x: x['number'])
        # カードをシャッフルする
        random.shuffle(self.card_list)

        # 交換1
        playerhand.pop(num1)
        playerhand.append(self.card_list.pop(0))

        # 交換２
        if num2 != None:
            playerhand.pop(num2-1)
            playerhand.append(self.card_list.pop(0))

        # 交換３
        if num3 != None:
            playerhand.pop(num3-2)
            playerhand.append(self.card_list.pop(0))

        change_comcards = self.comchange_select(comhand)
        if not change_comcards[0] == None:
            change_str = [d.get('string') for d in change_comcards]
            mutch_list = [self.c_str.index(d) for d in change_str]
            # 数字の昇順に並び替える
            mutch_list = sorted(mutch_list, reverse=True)
            # print(mutch_list)
            for d in mutch_list:
                comhand.pop(d)
                comhand.append(self.card_list.pop(0))
        # 手札最終表示
        print('-------after shuffle-------')
        # 数字の昇順に並び替える
        playerhand = sorted(playerhand, key=lambda x: x['number'])
        comhand = sorted(comhand, key=lambda x: x['number'])
        # print(playerhand)
        # print(comhand)
        print([d.get('string') for d in playerhand])
        print([d.get('string') for d in comhand])

        return playerhand, comhand


if __name__ == '__main__':

    mh = ChangeHand()
    check_1 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {
        'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}]
    check_2 = [{'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}, {
        'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}]
    check_3 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    check_4 = [{'number': 4, 'symbol': 'Clubs', 'string': 'ClubsJ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}, {'number': 0, 'symbol': 'Joker', 'string': 'Joker'}]

    playerhand, comhand = mh.change_cards(check_1, check_2, 2, None, None)
    # print(playerhand)
    # print(comhand)

    playerhand1, comhand1 = mh.change_cards(check_4, check_3, 2, None, None)
    # print(playerhand1)
    # print(comhand1)
