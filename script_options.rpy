# Определение персонажей игры.
define g_boy = Character('Мальчик', color='#c8ffc8', image='g_boy')
define g_dad = Character('Папа', color='#ff80ff', image='g_dad')
define g_mother = Character('Мама', color='00ffff', image='g_mother')
define g_mc = Character('Мальчик', color='#c8ffc8', image='g_mc')
define g_friend = Character('Денис', color='ff00ff', image='g_friend')
define g_professor = Character('Профессор', color='ffff00', image='g_professor')

# Координаты расположения спрайтов
init:
    $ show_item = Position(xalign=0.5, yalign=0.5)
    $ right_pos = Position(xalign=0.8, yalign=1.0)
    $ left_pos1 = Position(xalign=0.2, yalign=1.0)
    $ left_pos2 = Position(xalign=0.3, yalign=1.0)

# Переменные 
#
# Меню выбора истории
define friends = True
define school = True
define parents = True
define painting = True
