# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

ip = str('Ежемесячный финансовый отчёт ИП Иванов')
print(ip)
deb = int(input('Введите сумму выручки: '))
cred = int(input('Введите сумму расходов: '))
sum = deb - cred
print('Баланс: ', sum, 'руб.')
if deb >= cred:
    rent = sum/deb*100
    print('Рентабельность: ', ('%.2f' % rent), '%')
    pers = int(input('Введите количиство сотрудников: '))
    print('Ежемесячная прибыль каждого сотрудника: ', ('%.2f' % (sum/pers)), 'руб.')
else:
    print('ИП Иванов в долгах!!!')
