import random
resource = ['Спросил у Ленина Наверно да','Думаю Да','Спросил у собаки сказала нет','Подумай сам','Ветерок нашептал скорее всего нет']
question = ('Что ты хотел Спросить?','Что то надо?','Могу тебя послушать', 'Что то тревожит?')
ball = ['Пон','0-0',':3','🤔']
game = True
while game is True:
    a = random.randint (0,4)
    b = random.randint (0,2)
    c = random.randint (0,3)
    print (f'_/({ball[c]})\_')
    print (question[b])
    quest = input()
    print ('Ответ Кого то(=`ω´=)')
    if  quest == 'Выход':
        game = False
    elif quest == 'Можно мне поиграть в компьютер':
        print('Ты выучил Диаграммы,Значит Можно')
    print (resource[a])
    print ('-------------------------------------------------------------------')