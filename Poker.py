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
        
        card_list.append({
                    'number': 0,
                    'symbol': 'Joker',
                    'string': 'Joker'
                })
        self.card_list = card_list
        

    def shuffle(self):
        # カードをシャッフルする
        random.shuffle(self.card_list)

    # 手札を作成する
    def reset_draw_cards(self):
        card_list = self.make_card_list()

        number = 5

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

        # print(self.draw_cards)
        return self.draw_cards,self.draw_cards2,self.card_list

    
if __name__ == '__main__':
    tg = TrumpGame()
    cnt = 0
    draw_cards,draw_cards2,deck = tg.reset_draw_cards()
   
    print("プレイヤー　ハンド")
    for card in draw_cards:
        cnt += 1
        print(card['string'])
    print(cnt)

    print("敵　ハンド")
    for card in draw_cards2:
        cnt += 1
        print(card['string'])
    print(cnt)

    print("デッキ")
    for card in deck: #tg.card_listは残りのデッキ数
        cnt += 1
        print(card['string'])
    print(cnt)
