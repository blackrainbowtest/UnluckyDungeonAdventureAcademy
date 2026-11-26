# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character(_('Эйлин'), color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    call screen create_nyra

    if _return == "confirmed":
        jump academy_courtyard

    return
