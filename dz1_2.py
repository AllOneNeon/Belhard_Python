class InconsistentDataError (Exception):
    pass

try:
    d = list (map(int, input ("Введите несколько значений 2-х катетов через пробел: "). split ()))
    a = d[0::2]
    b = d[1::2]
    number = 1
    if len(d) % 2 == 0:
        for index in range (len(a)) and range (len(b)):
            e = int((a[index]**2 + b[index]**2) ** 0.5)
            s = int(a[index] * b[index]/2)
            print (f'Треугольник {number} с катетами {a[index]} и {b[index]} имеет площадь {s} и гипотенузу {e} \n')
            number += 1 
    else:
        raise InconsistentDataError ('Вы ввели нечетное количество катетов')
except ValueError:
        print('NonNumericError')

    
