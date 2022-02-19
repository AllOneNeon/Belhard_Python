class InconsistentDataError (Exception):
    pass

try:
    a = list(map(int, input('Значения одного катета n треугольников: ').split()))
    b = list(map(int, input('Значение второго катета n треугольников: ').split()))
    num = 0
    if len(a) == len(b):
        for index in range (len(a)) and range (len(b)):
            c = int((a[index]**2 + b[index]**2) ** 0.5)
            S = int(a[index]*b[index]/2)
            num += 1
            print(f'Треугольник {num} с катетами {a[index]} и {b[index]} имеет площадь {S} и гипотенузу {c}\n')
    else:
        raise InconsistentDataError ('Неравные массивы')
except ValueError:
        print('NonNumericError')