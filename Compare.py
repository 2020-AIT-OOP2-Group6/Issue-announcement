






# def check_poker_hand(self):
#     # ペア数
#     pair_count = 0
#     # 同じ数字のカウント
#     match_count = 0
#     # 同じ数字の枚数(3カード,4カードチェック用)
#     match_number = 0
#     # フラッシュの有無フラグ
#     flash_flag = True
#     # ストレートの有無フラグ
#     straight_flag = True

#     # 数字の昇順に並び替える
#     cards = sorted(self.draw_cards, key=lambda x: x['number'])

#     # 比較チェックループ
#     for i in range(1, 5):
#         # 前の数字が同じかチェック
#         if cards[i]['number'] == cards[i - 1]['number']:
#             match_count += 1
#             # 最終ループチェック
#             if i == 4:
#                 if match_count == 1:
#                     pair_count += 1
#                 # 3カード以上の場合
#                 elif match_count > 1:
#                     match_number = match_count + 1
#         else:
#             # 違う数字の場合
#             if match_count == 1:
#                 pair_count += 1
#             # 3カード以上の場合
#             elif match_count > 1:
#                 match_number = match_count + 1
#             match_count = 0
#         # 同じマークが続いているかチェック
#         if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
#             flash_flag = False
#         # 数字が連続しているかチェック
#         if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
#             if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
#                 straight_flag = False

#             # 最終手札チェック
#     if straight_flag == True and flash_flag == True:
#         if cards[0]['number'] == 1 and cards[4]['number'] == 13:
#             # ロイヤルストレートフラッシュ
#             hand = 700
#     elif match_number > 2:
#         if match_number == 4:
#             # 4カード
#             hand = 600
#         else:
#             if pair_count > 0:
#                 # フルハウス
#                 hand = 600
#             else:
#                 # 3カード
#                 hand = 500
#     elif straight_flag == True:
#         # ストレート
#         hand = 400
#     elif pair_count > 0:
#         if pair_count > 1:
#             # 2ペア
#             hand = 300
#         else:
#             # 1ペア
#             hand = 200
#     else:
#         # なし
#         hand = 100

#     return hand

# def check_poker_hand2(self):
#     # ペア数
#     pair_count = 0
#     # 同じ数字のカウント
#     match_count = 0
#     # 同じ数字の枚数(3カード,4カードチェック用)
#     match_number = 0
#     # フラッシュの有無フラグ
#     flash_flag = True
#     # ストレートの有無フラグ
#     straight_flag = True

#     # 数字の昇順に並び替える
#     cards = sorted(self.draw_cards2, key=lambda x: x['number'])

#     # 比較チェックループ
#     for i in range(1, 5):
#         # 前の数字が同じかチェック
#         if cards[i]['number'] == cards[i - 1]['number']:
#             match_count += 1
#             # 最終ループチェック
#             if i == 4:
#                 if match_count == 1:
#                     pair_count += 1
#                 # 3カード以上の場合
#                 elif match_count > 1:
#                     match_number = match_count + 1
#         else:
#             # 違う数字の場合
#             if match_count == 1:
#                 pair_count += 1
#             # 3カード以上の場合
#             elif match_count > 1:
#                 match_number = match_count + 1
#             match_count = 0
#         # 同じマークが続いているかチェック
#         if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
#             flash_flag = False
#         # 数字が連続しているかチェック
#         if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
#             if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
#                 straight_flag = False

#             # 最終手札チェック
#     if straight_flag == True and flash_flag == True:
#         if cards[0]['number'] == 1 and cards[4]['number'] == 13:
#             # ロイヤルストレートフラッシュ
#             hand = 'ロイヤル\nストレートフラッシュ'
#     elif match_number > 2:
#         if match_number == 4:
#             # 4カード
#             hand = 600
#         else:
#             if pair_count > 0:
#                 # フルハウス
#                 hand = 500
#             else:
#                 # 3カード
#                 hand = 400
#     elif straight_flag == True:
#         # ストレート
#         hand = 300
#     elif pair_count > 0:
#         if pair_count > 1:
#             # 2ペア
#             hand = 200
#         else:
#             # 1ペア
#             hand = 100
#     else:
#         # なし
#         hand = 0

#     return hand