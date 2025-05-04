# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

shifr = {'я':'*', 'г':'!', 'ш':'%', 'т':'-', 'и':':', 'р':'{', 'л':'7', 'ц':'52', ' ':'@'}
deshifr = {v: k for k, v in shifr.items()}
b = 'run'

def shifrat(shifr):
    while b != 'stop':
        a = input()
        if a == 'stop':
            b = a
        if a in shifr:
            print(shifr[a])


while True:
    com = input('shifrat ili deshifrat?')
    b = 'run'
    if com == 'shifrat':
        shifrat(shifr)
    elif com == deshifr:
        deshifrat
