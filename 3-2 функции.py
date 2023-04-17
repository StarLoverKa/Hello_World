# print()

# def a_fun():
#     ''' я простая функция'''
#     print('Привет. Я функция')
#
#
# a_fun()

# def empty_fun():
#     pass # вызов пустой функции
#
#
# empty_fun()

# a = 'hi!'
# def empty_fun():
#     print(a)
#
#
# empty_fun()

# def a_sum(x): # x - делает функцию универсальной
#             # вместо нее выводится любое значение
#     print(x)
#     a_sum = 0
#     for i in x:
#         a_sum += i
#     print('Сумма в списке: ',a_sum)
#
# a = [1,6,9,15,32]
# a_sum(a)
#
# b=[66,99,33]
# a_sum(b)

# def add(a,b):
#     print('a=',a,'b=',b)
#     return a+b # возврат функции
#
#
# # print(add(1,2))
# # print(add(1,3))
# # print(add(b=4,a=6))
# # x=add(b=7,a=3)
# # print(x)
# print(add(1,2))
# print(add('hi ','world'))
# print(add([1,2,3],[4,5,6]))

# def add(a=1,b=1): # значения по умолчанию
#     print('a=',a,'b=',b)
#     return a+b
#
# print(add())
# print(add(5)) #возможно менять значения по умолчанию
# print(add(5,5)) #возможно менять значения по умолчанию
# print(add(b=15))

# def add(e,a=1,b=1):
#     print('e=',e,'a=',a,'b=', b)
#     return a+b+e
#
#
# print(add(1))
# print(add(1,2,2))
# print(add(a=1,b=2,e=5))

# def many(*args,**kwargs):
#     print(args) # кортеж
#     for i in args:
#         print(i)
#     print(kwargs) #словарь
#     print(kwargs.values())
#
# many(1,2,3,'dda',a=12,b=34,c=43)

# def fun_a():
#     global a # глобальная, т.е. видимая везде
#     a=1
#     b=2
#     return a+b
#
# def fun_b():
#     c=3
#     return a+c
#
# print(fun_a())
# print(fun_b())

# def fun1(a,b):
#     def in_fun(x):
#         return x*x*x
#
#     return in_fun(a)+in_fun(b)
#
#
# print(fun1(4,5))

# def sum(a,b): return a+b
#
#
# print(sum(1,5))


# def season(a):
#     if 12==a<=2:
#         print('Время года - зима.')
#     elif 3<=a<=5:
#         print('Время года - весна.')
#     elif 6<=a<=8:
#         print('Время года - лето.')
#     elif 9<=a<=11:
#         print('Время года - зима.')
#
#
# season(a=int(input('Введите месяц года? ')))
