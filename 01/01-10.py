print('Добро пожаловать в Квест.')
print('Вы очнулись в незнакомом помещение')
print('Перед вами 3 двери с номерами: 1, 2 или 3.')
print('Дверь из которой можно выбраться - не крайняя, в какую пройдете?')
choice1 = input()
if choice1 == '3':
    print('Пройдя в эту дверь, она захлопнулась. Выхода нет. Не повезло.')
    choice2 = input()
    if choice2 == 'справа':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала ')
        print('Ловушка в стене, которая испепилила вас целиком!')
    elif choice2 == 'слева':
        print('За дверью оказался маленький милый кролик!Расслабившись, вы отвернулись, кролик напал на вас со спины. конец игры')
elif choice1 == '1':
    print('Вы упали в пропасть')
if choice1 == '2':
    print('Вы в следующей комнате')
    print('Выход отсюда возможен через 2 двери.')
    print('Дверь справа под номером 1, дверь слева под номером 2,')
    print('над дверью слева написано: выход в двери под номером 2.')
    print('Выход справа или слева?')
    otv2 = input()
    if otv2 == 'справа':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала ')
        print('гигантская подземная жаба, которая проглотила вас целиком!')
    elif otv2 == 'слева':
        print('Вы на улице!')