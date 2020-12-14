import Poker


hand_class = Poker.TrumpGame()

slist, olist, yamalist = hand_class.reset_draw_cards()
print(list)
print(type(list))
print(olist)
print(type(olist))

liststring = [d.get('string')for d in slist]
listolist = [d.get('string')for d in olist]
listyamalist = [d.get('string')for d in yamalist]

print(liststring)
print(listolist)
print(listyamalist)

for index, target_list in enumerate(liststring):

    liststring[index] = 'static/'+target_list+'.png'

    pass
print(liststring[0])
