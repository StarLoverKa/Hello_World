def card(a):
    return '*' * len(a[:-4]) + a[-4:]

a=int(input('Введите номер карты: '))
a1=str(a)
print(card(a1))



