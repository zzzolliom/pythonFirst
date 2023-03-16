
try:
    fingers=int(input('количество пальцев'))
except:
    print('error')
    fingers=2

if fingers==1:
     print('штрафная')
elif fingers==2:
    print('обычный бросок')
elif fingers==3:
    print('трехочковый')
else:
    print('а в баскетбол ли ты играешь, дружок?')