<<<<<<< Updated upstream
=======
import statistics
class CompareHand:#(coh)
    #役のチェック処理
    def __init__(self, check_joker = False):
        self.check_joker = check_joker
    def check_poker_hand(self, draw_cards): 
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

        # 数字の昇順に並び替える
        cards = sorted(draw_cards, key=lambda x: x['number'])
        #jockerの有無を判定
        if cards[0]['number'] == 0:
            self.check_joker = True
            #high_suit = [d.get('symbol') for d in draw_cards]
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
                    # 2ペアつまり３カード
                    hand = 300
                else:
                    # 1ペアつまり３カード
                    hand = 300
            else:
                # なしだがストレートになる
                hand = 400
            return hand
        else:
            #high_suit = [d.get('symbol') for d in draw_cards]
            # 比較チェックループ
            for i in range(1, 5):
                # 前の数字が同じかチェック
                if cards[i]['number'] == cards[i - 1]['number']:
                    match_count += 1
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
                if cards[0]['number'] == 1 and cards[4]['number'] == 5:
                    # ロイヤルストレートフラッシュ
                    hand = 700
            elif match_number > 2:
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
            elif straight_flag == True:
                # ストレート
                hand = 400
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



    def check_high_number(self, check_cards, hand):
        if(self.check_joker == True): # Joker有
            if(hand == 800): # ファイブカード（800点）：4枚同じ数字＋Joker
                y = 5
            elif(hand == 700): # ロイヤルストレートフラッシュ（700点）：4枚違う数字＋すべて同じマーク＋Joker
                y = 5
            elif(hand == 400): # ストレート（400点）：4枚違う数字＋Joker
                y = 5
            else:
                cards_number = [d.get('number') for d in check_cards]
                cards_number_sort = sorted(cards_number,reverse=True)
                print(cards_number_sort) 
                y = statistics.mode(cards_number_sort)
            
            # cards_number = [d.get('number') for d in check_cards]
            # cards_number_sort = sorted(cards_number,reverse=True)
            # y = statistics.mode(cards_number_sort)

            return y
        else:
            cards_number = [d.get('number') for d in check_cards]
            ards_number_sort = sorted(cards_number,reverse=True)
            y = statistics.mode(cards_number_sort)
            return y



        






   

if __name__ == "__main__":
    coh = CompareHand()
    check_1 = [{'number': 1, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 2, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 4, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 0, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    check_2 = [{'number': 1, 'symbol': 'Clubs', 'string': 'ClubsQ'}, {'number': 3, 'symbol': 'Hearts', 'string': 'HeartsQ'}, {'number': 1, 'symbol': 'Hearts', 'string': 'HeartsA'}, {'number': 3, 'symbol': 'Spades', 'string': 'SpadesQ'}, {'number': 1, 'symbol': 'Diamonds', 'string': 'DiamondsQ'}]
    hand1 = coh.check_poker_hand(check_1)
    hand2 = coh.check_poker_hand(check_2)
    print(hand1)#Jあり
    print(hand2)#Jなし
    print(coh.check_high_number(check_1, hand1))
    print(coh.check_high_number(check_2, hand2))

>>>>>>> Stashed changes
