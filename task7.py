# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

per = {'a': 100, 'b': 200, 'c':300}
vtor = {'a': 300, 'b': 200, 'd':400}

res = {}

for i in per:
    res[i] = per[i]

print(res)

for i in vtor:
    if i in res:
        res[i] += vtor[i]
    else:
        res[i] = vtor[i]

print(res)
