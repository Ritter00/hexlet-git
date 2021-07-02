print('Добро, пожаловать в игру "крестики-нолики"')
player_name1 ='Vasya' #input('Введите имя первого игрока: ')
player_name2 ='Petruxa' #input('Введите имя второга игрока: ')
size_field =3 #int(input('Введите размер поля для игры(число): '))
print(player_name1,'(ходит "крестиками" - Х),',player_name2,'(ходит "ноликами" - O)')
print(
    '''Правила игры следующие:
    введитете номер поля
    '''
)

field = [['-' for i in range(size_field + 1)]for j in range(size_field + 1)]
for i in range(0,len(field[0])):
    field[0][i] = i
for i in range(0, len(field)):
    field[i][0] = i
field[0][0] = ' '

def print_field(f):
    print('____' * (size_field+1))
    for i in f:
        for j in i:
            print('| {: ^2}'.format(j), end='')
        print('|')
    print('____' * (size_field+1))
print_field(field)
def player_1(s):
    a = int(input(f'{player_name1}, ведите номер стобца: '))
    b = int(input(f'{player_name1}, ведите номер строки: '))
    if s[b][a] not in ['O', 'X']:
        s[b][a]='X'
    else:
        print('Неверно введено число')
        return player_1
player_1(field)

print_field(field)
player_1(field)
print_field(field)