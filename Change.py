
class ChangeHand:

    def receive_my_hand(self, drawcards, card_decks ,num1,num2,num3):
        
        #手札格納
        my_hand=[]
        for i in drawcards:
            my_hand.append(i)
        
        self.my_hand=my_hand
        #手札表示
        print(self.my_hand)

        #デッキ格納
        deck_list=[]
        for i in card_decks:
            deck_list.append(i)
        
        self.deck_list=deck_list

        #残りのデッキ一覧表示
        print(self.deck_list)

        #交換1
        self.my_hand.pop(num1)
        self.my_hand.append(self.deck_list.pop(0))

        #交換２
        if num2 != None:
            self.my_hand.pop(num2-1)
            self.my_hand.append(self.deck_list.pop(0))

        #交換３
        if num3 != None:
            self.my_hand.pop(num3-2)
            self.my_hand.append(self.deck_list.pop(0))

        #手札最終表示
        print(self.my_hand)

   

if __name__ == '__main__':
    
    mh=ChangeHand()
    #mh.receive_my_hand([1,2,3,4,5],[6,7,8,9] , 2 ,None,None)
    #mh.receive_my_hand([1,2,3,4,5],[6,7,8,9] , 2 ,3,None)
    mh.receive_my_hand([1,2,3,4,5],[6,7,8,9] , 2 ,3,4)
    

    

   

    