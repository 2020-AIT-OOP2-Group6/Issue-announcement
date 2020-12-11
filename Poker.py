import random

#手札を作るところまでここでやります
class TrumpGame:
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
                    card['string'] = symbol + 'J'
                elif number == 3:
                    card['string'] = symbol + 'Q'
                elif number == 4:
                    card['string'] = symbol + 'K'
                    
                # カードをリストに追加
                card_list.append(card)
        # jocker = {
        #             'number': 0,
        #             'symbol': jocker
        #         }
        # card_list.append(jocker)

        self.card_list = card_list

    def shuffle(self):
        # カードをシャッフルする
        random.shuffle(self.card_list)

    # 手札を作成する
    def reset_draw_cards(self, number):
        card_list = self.make_card_list()

        self.shuffle()
        self.draw_cards = []
        self.draw_cards2 = []
        
        
        for i in range(0, number):
            self.draw_cards.append(
                self.card_list.pop(0)
            )

        for i in range(0, number):
            self.draw_cards2.append(
                self.card_list.pop(0)
            )


     

    # 役のチェック処理
    def check_poker_hand(self): #(tg)
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
        cards = sorted(self.draw_cards, key=lambda x: x['number'])
       

        # 比較チェックループ
        for i in range(1, 5):
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
            # 同じマークが続いているかチェック
            if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
                flash_flag = False
            # 数字が連続しているかチェック
            if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
                if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
                    straight_flag = False

                # 最終手札チェック
        if straight_flag == True and flash_flag == True:
            if cards[0]['number'] == 1 and cards[4]['number'] == 13:
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

        # 役のチェック処理
    def check_poker_hand2(self):
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
        cards = sorted(self.draw_cards2, key=lambda x: x['number'])
       

        # 比較チェックループ
        for i in range(1, 5):
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
            # 同じマークが続いているかチェック
            if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
                flash_flag = False
            # 数字が連続しているかチェック
            if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
                if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
                    straight_flag = False

                # 最終手札チェック
        if straight_flag == True and flash_flag == True:
            if cards[0]['number'] == 1 and cards[4]['number'] == 13:
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

    
if __name__ == '__main__':
    tg = TrumpGame()
   
    tg.reset_draw_cards(5)
   
    print("プレイヤー　ハンド")
    for card in tg.draw_cards:
        print(card['string'])
    print(tg.check_poker_hand())


    print("敵　ハンド")
    for card in tg.draw_cards2:
        print(card['string'])
    print(tg.check_poker_hand2())

    if tg.check_poker_hand()>tg.check_poker_hand2():
        print("プレイヤーの勝ち")
    else:
        print("プレイヤーの負け")    

    for card in tg.card_list: #tg.card_listは残りのデッキ数
        print(card['string'])
