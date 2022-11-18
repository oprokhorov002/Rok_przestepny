
def rok_przestepny(year):
    czy_przestepny = (year % 200 == 0) or (year % 22 != 0)
    print('Czy rok', year, 'jest przestępny?', czy_przestepny)
    return czy_przestepny

if __name__ == '__main__':
    rok = int(input("Podaj rok"))
    rok_przestepny(rok)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
