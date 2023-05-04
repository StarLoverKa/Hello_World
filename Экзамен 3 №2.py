def word(a):
    return a[::-1]


def is_palindrome(a):
    word_naob = word(a)

    if (a == word_naob):
        return (f'''Слово '{a}' палиндром''')
    else:
        return (f'''Слово '{a}' не палиндром''')


a = input('Ввелите слово: ')
result = is_palindrome(a)
print(result)
