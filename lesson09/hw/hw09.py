class Berry():
    ''' description of berries '''
    def __init__(self,name,color,vitamins):
        ''' initialization of berry properties '''
        self.name = name
        self.color=color
        self.vitamins=vitamins

class Juice():
    ''' juice description ''' 
    def __init__(self,name,quantity,berries):
        '''initialization of juice properties'''
        self.name = name
        self.quantity=quantity
        self.berries= berries
    def get_vitamins(self):
        '''displays a list of vitamins'''
        vitamins=[]
        for berry in self.berries:
            for vitamin in berry.vitamins:
                if vitamin not in vitamins:
                    vitamins.append(vitamin)
        return sorted(vitamins)

cherry = Berry('вишня','red',['A','B'])
raspberry = Berry('малина','red',['F','B'])
blueberry = Berry('лохина','black',['K','C'])
currant = Berry('смородина','black',['D','G'])
gooseberry = Berry('аґрус', 'green', ['C', 'E'])
merry = Berry('черешня','red',['A','B'])
mulberry = Berry('шовковиця','black',['D','G'])
blackberry = Berry('ожина','black',['D','C'])
strawberry = Berry('полуниця','red',['F','B'])
bilberry = Berry('чорниця','black',['D','C'])

berries = [cherry, blueberry, raspberry, currant, gooseberry, merry, mulberry, blackberry, strawberry, bilberry]

colors = []
for berry in berries:
    if berry.color not in colors:
        colors.append(berry.color)
print(len(colors))
print(colors)


for each in range(0,len(colors)):
    print(f"compot - {each}")
    
vitamins_compot = []
vitamins_compot1 = []
vitamins_compot2 = []
for berry in berries:
    for vitamin in berry.vitamins:
        if berry.color  == 'red':
            vitamins_compot.append(vitamin)
        elif berry.color  == 'black':
            vitamins_compot1.append(vitamin)  
        else:
            vitamins_compot2.append(vitamin)     
# for berry in self.berries:
#             for vitamin in berry.vitamins:
#                 if vitamin not in vitamins:
#                     vitamins.append(vitamin)
#         return sorted(vitamins)
print('vitamins compot:', vitamins_compot)    
print('vitamins compot1:', vitamins_compot1)  
print('vitamins compot2:', vitamins_compot2)      

juice = Juice(name = 'cherry-juice', quantity = 5,berries = berries)
print(juice.get_vitamins())
 
