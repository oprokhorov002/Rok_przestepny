rok = int(input('Podaj rok: '))
czy_przestepny = (rok % 400 == 0) or (rok % 100 != 0) and (rok % 4 == 0)
print('Czy rok', rok, 'jest przestępny?', czy_przestepny)
print("Hello")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
