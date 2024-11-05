from random import randint
print("Казино Большой Вулкан 666 выводы за секунду")
bank = 20
while bank>0 and bank<300:
    bet = 0
    print()
    print("На твоём счету ",bank," бублей")
    bet = int(input("Твоя ставка: "))
    print()
    if bet>bank or bet<=0:
        continue
    bank -= bet
    a = randint(1,100)
    if 5<a<15:
        print("Ничего")
        bank += bet
    if 15<=a<56:
        print("Выиграл")
        bet *= 2
        bank += bet
    if 56<=a<100:
        print("Проиграл")
    if a==100 or a<=5:
        print("Джекпот!")
        bet = bet*10
        bank += bet
        print("На твоём счету ",bank," бублей")

if bank >= 100:
    print()
    print("Ты выиграл слишком много, и тебя ограбили. :(")
elif bank <= 0:
    print()
    print("Ты всё проиграл. :(")
else:
    print()
    print("Я не знаю, что случилось, ты проиграл из-за бага. :(")
