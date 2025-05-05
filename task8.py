# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

shifr = {'я':'*', 'г':'!', 'ш':'%', 'т':'-', 'и':':', 'р':'{', 'л':'7', 'ц':'5', ' ':'@'}
deshifr = {v: k for k, v in shifr.items()}
b = 'run'

def shifrat(shifr):
    while True:
        res = []
        a = input()
        for i in a:
            if i in shifr:
                res.append(shifr[i])
        print(''.join(res))
        if a == 'выход':
            break

def deshifrat(deshifr):
    while True:
        res = []
        a = input()
        for i in a:
            if i in deshifr:
                res.append(deshifr[i])
        print(''.join(res))
        if a == 'выход':
            break

while True:
    com = input('shifrat ili deshifrat?')
    b = 'run'
    if com == 'shifrat':
        shifrat(shifr)
    elif com == 'deshifrat':
        deshifrat(deshifr)
