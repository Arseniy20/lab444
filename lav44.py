a = int(input('Введите число: '))
if (a % 3  == 0):
    print('Число делится на три')
else:
    print('Число не делится на три')

def lab2():
    a = int(input('Число: '))
    try:
        a = (a)
        a/100
        if a == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Введена строка, попробуй ещё раз')
    else:
        print(a/100)
lab2()


def lab3():
    print('Введите дату через пробел ДД ММ ГГГГ:')
    def is_magic_date(day, month, year):
        return day * month == year % 100

    d, m, y = map(int, input().split())
    print(is_magic_date(d, m, y))

lab3()

def lab4():
    a = list(map(int, input('Введите номер билета: ')))
    if len(a) % 2 == 1:
        print("Введите четное количество чисел!")
    elif sum(a[:len(a) // 2]) == sum(a[len(a) // 2:]):
        print("Счастливый билет!")
    else:
        print("Не счастливый(")
lab4()
