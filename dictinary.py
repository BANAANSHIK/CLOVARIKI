print('hi world')
user = {
    'username': "Artyrvv0",
    'pasword': 123,
    'robux': 1,
    'gender': 'male'
}
# print(' your name is', user['username'])
# print('you robux balance is', user['robux'])

# print(user.get('grobux')) #тоже самое что и в крвадратных скобках
# print(user.items()) #возвращает вместа себя массив кортежей
# print(user.keys())# словарь превращается в массив в левой стороне
# print(user.pop())# удаляет любой написынный эллимент в словаре
# print(user.values)# словарь превращается в массив в правой стороне
# user['gender']# добавляет в словарь что либо
#user.setdefualt ('new key', ' my bou')# добавдяет в словарь новое значение более круто чем верхнее
enemy = {
    'hp':100,
    'damage':10,
    'name':'ORK'
}




player = {
    'hp':130,
    'damage':15,
    'name': "нежнейший при нежный ЧЁРТ"
}


def fight(player, enemy):
    print(f'игрок{player["name"]} атакует {enemy["name"]} и наносит {player["damage"]}')
    enemy["hp"] -= player['damage']
    print(f'у {enemy["name"]} осталось {enemy["hp"]} здоровья')
fight(player,enemy)

