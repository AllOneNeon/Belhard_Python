persons = [{'name': 'Andrei', 'age': 23, 'sex': 'male'}, {'name': 'Tati', 'age': 16, 'sex': 'female'}]
num_people = []
for i in persons:
    num_people.append(i['name'])
print('Количество людей: ' , len(num_people))
num_male = [xy for xy in persons if xy['sex'] == 'male']
print('Количество мужчин: ' , len(num_male))
num_female = [xx for xx in persons if xx['sex'] == 'female']
print('Количество женщин: ' , len(num_female))
num_of_legal_age = [d for d in persons if d['age'] > 18]
print ('Количество совершеннолетних лиц: ' , len (num_of_legal_age))
num_name = []
for n in persons:
    num_name.append(n['name'])
print('Использованные имена: ', num_name)
num_age = []
for a in persons:
    num_age.append(a['age'])
    num_age.sort ()
print('Список возрастов: ', num_age)
from collections import Counter
num_common = []
for c in persons:
    num_common.append(c['name'])
print('3 самых встречающихся имени: ', [element for element, count in Counter(num_common).most_common(3)])
male_names = [mn for mn in persons if mn['sex'] == 'male' and mn['age'] > 35 and mn['name'][0] =='F']
names = [mn['name'] for mn in male_names]
print('Имена мужчин старше 35 лет, чье имя начинается с буквы F: ' , names)