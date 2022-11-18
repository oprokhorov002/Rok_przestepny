def rok_przestepny(year):
    czy_przestepny = (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)
    print('Czy rok', year, 'jest przestępny?', czy_przestepny)
    return czy_przestepny


if __name__ == '__main__':
    rok = int(input("Podaj rok"))
    rok_przestepny(rok)


def test_rok_ma_byc_przystepny():
    assert rok_przestepny(2020) == True


def test_rok_ma_byc_nieprzystepny():
    assert rok_przestepny(2022) == False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
