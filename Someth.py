###1 vazifa
# num1 = int(input('Birinchi raqamni kiriting: '))
# num2 = int(input('Ikkinchi raqamni kiriting: '))
# num3 = int(input('Uchinchi raqamni kiriting: '))
#
# if num2 < num1 < num3 or num3 < num1 < num2:
#     print(num1)
# elif num1 < num2 < num3 or num3 < num2 < num1:
#     print(num2)
# else:
#     print(num3)

# age = int(input('Yoshingizni kirg\'izing: '))
# if age <= 18:
#     print('O\'qishingiz kerak')
# elif 18 < age <= 50:
#

### List - Ro'yxat - Список
# products = [1, 's', 1.3, True, False]
# lst = list()
# print(type(products))
# print(type(lst))
# print(lst)
# print(type(True))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # index - bu tartib raqami
# print(len(lst))
# print(len('ABDURAHMON'))
# print(lst[0])
# print(lst[4])
# print(lst[-1])
# print(lst[-2])
# lst[0] = 's'
# print(lst)

# cars = ['gentra','hyundai', 'mers' ,'hongi']
# print(cars.index('hyundai'))
# print(cars.count('hyundai'))

# cars.append('bugatti')  #append listni ohiriga qo'shish
# print(cars)
# cars.insert(2, 'matiz')
# print(cars)
# cars.insert(-1, 'cobalt')
# print(cars)

# del cars[0]
# print(cars)

# print(cars)
# cars.remove('gentra')
# print(cars)

# deleted_car = cars.pop(0)
# print(cars)
# print(deleted_car)

lst = [3, 2, 16, 12, 4, 5, 1, 7]
lst.sort()
print(lst)
print(lst[2])
lst.sort(reverse=True)
print(lst)
print(sorted(lst))
print(lst[2])

