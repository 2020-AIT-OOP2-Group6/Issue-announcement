import pandas as pd

class CompareHand:#(coh)

    def judge_card(self,playerhand,comhand):
        # マークのリスト
        symbol_list = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

        # 数字の昇順に並び替える
        playerhand = sorted(playerhand, key=lambda x: x['number'])
        comhand = sorted(comhand, key=lambda x: x['number'])
        # 手札を見やすく
        # print([d.get('string') for d in playerhand])
        # print([d.get('string') for d in comhand])

        mode_p_card = pd.DataFrame(playerhand)['number'].mode().tolist()
        mode_c_card = pd.DataFrame(comhand)['number'].mode().tolist()
        #　ツーペアの場合
        mode_p_card.sort()
        mode_c_card.sort()
        high_p_card = mode_p_card[0]
        high_c_card = mode_c_card[0]

        # 値の小さいほうが強い手
        # print(f'player_highcard:{mode_p_card},com_highcard:{mode_c_card}')

        if playerhand[0]['number'] == 0:
            #jokerアリの場合(player)
            p_point = self.joker_handpoint(playerhand)
            c_point = self.handpoint(comhand)
        elif comhand[0]['number'] == 0:
            #jokerアリの場合(com)
            c_point = self.joker_handpoint(comhand)
            p_point = self.handpoint(playerhand)
        else:
            #joker無しの場合
            p_point = self.handpoint(playerhand)
            c_point = self.handpoint(comhand)

        # print(p_point)
        # print(c_point)
        #　フォーカード
        if p_point > c_point:
            return 'player',p_point
        elif p_point < c_point:
            return 'com',c_point
        else:
            #　フルハウス、スリーカード
            if high_p_card < high_c_card:
                return 'player',p_point
            elif high_p_card > high_c_card:
                return 'com',p_point
            else: #　ツーペア、ワンペア
                # ユニークなもののみ
                playerhand = [x for x in playerhand if not x['number'] == mode_p_card[0]]
                comhand = [x for x in comhand if not x['number'] == mode_c_card[0]]
                # print([d.get('string') for d in playerhand])
                # print([d.get('string') for d in comhand])
                if not len(mode_p_card)==1 and not len(mode_c_card)==1:
                    # ツーペア
                    # さらにユニークなもののみ
                    playerhand = [x for x in playerhand if not x['number'] == mode_p_card[1]]
                    comhand = [x for x in comhand if not x['number'] == mode_c_card[1]]
                    # print([d.get('string') for d in playerhand])
                    # print([d.get('string') for d in comhand])
                    if mode_p_card[1] < mode_c_card[1]:
                        return 'player',p_point
                    elif mode_p_card[1] > mode_c_card[1]:
                        return 'com',p_point
                    else: # キック（スート含む）
                        p_num = [d.get('number') for d in playerhand]
                        c_num = [d.get('number') for d in comhand]
                        #　スート（数字の小さいほうが強い）
                        p_symbol = symbol_list.index([d.get('symbol') for d in playerhand][0])
                        c_symbol = symbol_list.index([d.get('symbol') for d in comhand][0])
                        if p_num[0] < c_num[0]:
                            return 'player',p_point
                        elif p_num[0] > c_num[0]:
                            return 'com',p_point
                        else:
                            if p_symbol < c_symbol:
                                return 'player',p_point
                            elif p_symbol > c_symbol:
                                return 'com',p_point
                else:
                    # キック（スート含む）
                    p_num = [d.get('number') for d in playerhand]
                    c_num = [d.get('number') for d in comhand]
                    #　スート（数字の小さいほうが強い）
                    p_symbol = symbol_list.index([d.get('symbol') for d in playerhand][0])
                    c_symbol = symbol_list.index([d.get('symbol') for d in comhand][0])
                    if p_num[0] < c_num[0]:
                        return 'player',p_point
                    elif p_num[0] > c_num[0]:
                        return 'com',p_point
                    else:
                        if p_symbol < c_symbol:
                            return 'player',p_point
                        elif p_symbol > c_symbol:
                            return 'com',p_point
                    
            return 'drow',p_point

    def handpoint(self, cards):
        #ファイブカード、ロイヤルストレートフラッシュ、ストレートの可能性はない

        # ペア数
        pair_count = 0
        # 同じ数字のカウント
        match_count = 0
        # 同じ数字の枚数(3カード,4カードチェック用)
        match_number = 0

        # 比較チェックループ
        for i in range(1, 5):#1,2,3,4
            # 前の数字が同じかチェック
            if cards[i]['number'] == cards[i - 1]['number']:
                match_count += 1
                # 最終ループチェック
                if i == 4:
                    if match_count == 1:
                        pair_count += 1
                    # 3カード以上の場合
                    elif match_count > 1:
                        match_number = match_count + 1
            else:
                # 違う数字の場合
                if match_count == 1:
                    pair_count += 1
                # 3カード以上の場合
                elif match_count > 1:
                    match_number = match_count + 1
                match_count = 0

        # 最終手札チェック
        if match_number > 2:
            if match_number == 4:
                # 4カード
                hand = 600
            else:
                if pair_count > 0:
                    # フルハウス
                    hand = 500
                else:
                    # 3カード
                    hand = 300
        elif pair_count > 0:
            if pair_count > 1:
                # 2ペア
                hand = 200
            else:
                # 1ペア
                hand = 100
        else:
            # なし
            hand = 0
        
        return hand

    def joker_handpoint(self, cards):
        # ペア数
        pair_count = 0
        # 同じ数字のカウント
        match_count = 0
        # 同じ数字の枚数(3カード,4カードチェック用)
        match_number = 0
        # フラッシュの有無フラグ
        flash_flag = True
        # ストレートの有無フラグ
        straight_flag = True
        # 比較チェックループ
        for i in range(2, 5):
            # 前の数字が同じかチェック
            if cards[i]['number'] == cards[i - 1]['number']:
                match_count += 1
                #揃っていてかつ大きな方のスートを保持
                #high_suit_get = append(high_suit[i])
                # 最終ループチェック
                if i == 4:
                    if match_count == 1:
                        pair_count += 1
                    # 3カード以上の場合
                    elif match_count > 1:
                        match_number = match_count + 1
            else:
                # 違う数字の場合
                if match_count == 1:
                    pair_count += 1
                # 3カード以上の場合
                elif match_count > 1:
                    match_number = match_count + 1
                match_count = 0
            # 同じマークが続いているかチェック
            if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
                flash_flag = False
            # 数字が連続しているかチェック
            if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
                if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
                    straight_flag = False

        # 最終手札チェック
        if straight_flag == True and flash_flag == True:
            #ロイヤルストレートフラッシュ
            hand = 700
        elif match_number > 2:

            if match_number == 4:
                # 4カードなので５カードになる
                hand = 800
            else:
                if pair_count > 0:
                    # フルハウス
                    hand = 500
                else:
                    # 3カードつまり４カードになる
                    hand = 600
        elif straight_flag == True:
            # ストレート
            hand = 400
        elif pair_count > 0:
            if pair_count > 1:
                # 2ペアつまりフルハウス
                hand = 500
            else:
                # 1ペアつまり３カード
                hand = 300
        else:
            # なしだがストレートになる
            hand = 400
        return hand


if __name__ == "__main__":
    coh = CompareHand()
    # check_1 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    # check_2 = [{'number': 4, 'symbol': 'Clubs', 'string': 'ClubsJ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}, {'number': 0, 'symbol': 'Joker', 'string': 'Joker'}]
    # #フォーカード
    # print(coh.judge_card(check_1,check_2))#playerはQのフォーカード、comはJ+Jokerのフォーカード

    # check_3 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    # check_4 = [{'number': 4, 'symbol': 'Clubs', 'string': 'ClubsJ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}]
    # # フォーカード
    # print(coh.judge_card(check_4,check_3))#playerはJのフォーカード、comはQのフォーカード

    # check_5 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}]
    # check_6 = [{'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}]
    # #フルハウス
    # print(coh.judge_card(check_5,check_6))#playerはQのスリーカード、comはKのスリーカード

    # check_7 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 0, 'symbol': 'Joker', 'string': 'Joker'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}]
    # check_8 = [{'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}]
    # #フルハウス
    # print(coh.judge_card(check_8,check_7))#playerはKのスリーカード、comはQ+Jokerのスリーカード

    # check_9 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Herats', 'string': 'HeratsQ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeratsA'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}]
    # check_10 = [{'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}]
    # #ツーペア（前ペア違い）
    # print(coh.judge_card(check_9,check_10))#playerはAQのツーペア、comはKJのツーペア

    # check_11 = [{'number': 1, 'symbol': 'Clubs', 'string': 'ClubsA'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 4, 'symbol': 'Diamonds', 'string': 'DiamondsJ'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}]
    # check_12 = [{'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 2, 'symbol': 'Diamonds', 'string': 'DiamondsK'}]
    # #ツーペア（次ペア違い）
    # print(coh.judge_card(check_11,check_12))#playerはAQのツーペア、comはKJのツーペア

    # check_13 = [{'number': 1, 'symbol': 'Clubs', 'string': 'ClubsA'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}]
    # check_14 = [{'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 2, 'symbol': 'Diamonds', 'string': 'DiamondsK'}]
    # #ツーペア（キッカーあり、スートなし）
    # print(coh.judge_card(check_13,check_14))#playerはAKのツーペアQ、comはAKのツーペアJ

    # check_15 = [{'number': 1, 'symbol': 'Clubs', 'string': 'ClubsA'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 2, 'symbol': 'Clubs', 'string': 'ClubsK'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}]
    # check_16= [{'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 2, 'symbol': 'Diamonds', 'string': 'DiamondsK'}]
    # #ツーペア（キッカーあり、スートあり）
    # print(coh.judge_card(check_15,check_16))#playerはAKのツーペアHeartsQ、comはAKのツーペアDiamondQ

    # check_17 = [{'number': 3, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsK'}, {'number': 4, 'symbol': 'Hearts', 'string': 'HeartsJ'}]
    # check_18 = [{'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 3, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}, {'number': 1, 'symbol': 'Spades', 'string': 'SpadesA'}, {'number': 2, 'symbol': 'Spades', 'string': 'SpadesK'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesJ'}]
    # #ワンペア(キッカーあり、スートあり)
    # print(coh.judge_card(check_17,check_18))#playerはQのワンペアHeartsAKJ、comはQのワンペアSpadesAKJ

    check_19 = [{'number':0,"symbol":'Joker','string':'Joker'}, {'number':1,'symbol':'Hearts','string':'HeartsA'}, {'number':1,'symbol':'Spades','string':'SpadesA'}, {'number':3,'symbol':'Diamonds','string':'DiamondsQ'}, {'number':3,'symbol':'Hearts','string':'HeartsQ'}]
    check_20 = [{'number':2,'symbol':'Diamonds','string':'DiamondsK'}, {'number':2,'symbol':'Hearts','string':'HeartsK'}, {'number':2,'symbol':'Clubs','string':'ClubsK'}, {'number':4,'symbol':'Spades','string':'SpadesJ'}, {'number':4,'symbol':'Diamonds','string':'DiamondsJ'}]
    print(coh.judge_card(check_19,check_20))