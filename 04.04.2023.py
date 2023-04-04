import random
NumList=["Джокер", "2", "3","4","5","6","7","8","9","10","Валет","Дама","Король","Туз"]
MastList= ["Пик", "Крестей", "Бубей", "Червей"]
class DeckOfCards:

    def __init__(self):
        self.deck=[]
        for num in NumList:
            for mast in MastList:
                self.deck.append((num, mast))

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self,index):
        if len(self.deck) > 0:
            print(self.deck[index])
            #self.deck.pop[index] ---не удаляется
            return self.deck[index]
        else:
            return "Карты кончились "


cards=DeckOfCards()
cards.shuffle()
cards.get(5)








