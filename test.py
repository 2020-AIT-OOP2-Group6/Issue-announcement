import Type_Adjust
import Compare

list = []

list += ['1', 'null', 'null']

for i, target_list in enumerate(list):

    if target_list == 'null':
        list[i] = None


print(list)

hand_list = ['Joker', 'HeartsA', 'SpadesA', 'DiamondsQ', 'HeartsQ']
ophand_list = ['DiamondsK', 'HeartsK', 'ClubsK', 'SpadesJ', 'DiamondsJ']
hand_dictionary = []
for hand in hand_list:
    hand_dictionary.append(Type_Adjust.Adjust(hand))

print(hand_dictionary)

ophand_dictionary = []
for ophand in ophand_list:
    ophand_dictionary.append(Type_Adjust.Adjust(ophand))

print(ophand_dictionary)

# 外部クラスのインスタンス
coh = Compare.CompareHand()

# 勝敗判断
judge, hand_score = coh.judge_card(hand_dictionary, ophand_dictionary)

print(judge,hand_score)
        


