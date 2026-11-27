#   ____  ____  _     ___ _____ ____  _   _    _    ____  ____    ____ _____ _   _ ____ ___ ___
#  / ___||  _ \| |   |_ _|_   _/ ___|| | | |  / \  |  _ \|  _ \  / ___|_   _| | | |  _ \_ _/ _ \
#  \___ \| |_) | |    | |  | | \___ \| |_| | / _ \ | |_) | | | | \___ \ | | | | | | | | | | | | |
#   ___) |  __/| |___ | |  | |  ___) |  _  |/ ___ \|  _ <| |_| |  ___) || | | |_| | |_| | | |_| |
#  |____/|_|   |_____|___| |_| |____/|_| |_/_/   \_\_| \_\____/  |____/ |_|  \___/|____/___\___/

# /* ******************************************************************************************************** */
# /*                                                                                                          */
# /*   File: C:\renpy\games\UnluckyDungeonAdventureAcademy\game\character_creation.rpy                        */
# /*                                                        /\_/\                                             */
# /*                                                       ( •.• )                                            */
# /*   By: unluckydungeonadventure.gmail.com                > ^ <                                             */
# /*                                                                                                          */
# /*   Created: 2026/11/27 01:09:19 by UDA                                                                    */
# /*   Updated: 2026/11/27 01:09:19 by UDA                                                                    */
# /*                                                                                                          */
# /* ******************************************************************************************************** */


# game/character_creation.rpy

# Названия характеристик.
define nyra_stat_labels = [
    ("atk", _("Атака")),
    ("def", _("Защита")),
    ("matk", _("Магическая атака")),
    ("mdef", _("Магическая защита")),
    ("eva", _("Уклонение")),
    ("spd", _("Скорость")),
    ("vit", _("Выносливость")),
    ("mana", _("Магический запас"))
]


init python:

    def change_nyra_stat(stat, amount):

        if stat not in player["stats"]:
            return

        current = player["stats"][stat]
        points = player["free_points"]

        if amount == 1:
            if points <= 0:
                return

        elif amount == -1:
            if current <= 5:
                return

        else:
            return

        player["stats"][stat] += amount
        player["free_points"] -= amount

    def valid_nyra_name(name):
        name = name.strip()
        if not name:
            return True

        for char in name:
            if not (char.isalpha() or char in " -"):
                return False

        return any(char.isalpha() for char in name)



screen create_nyra():

    modal True

    default open_category = None

    add "gui/character_creation/backgrounds/character_creation_bg.png"

    text _("Создание персонажа"):
        pos (540, 148)
        anchor (0.5, 0.5)
        size 42

    $ selected_avatar = nyra_avatars.get(player["avatar"])
    fixed:
        pos (542, 384)
        anchor (0.5, 0.5)
        xysize (400, 358)

        if selected_avatar and renpy.loadable(selected_avatar):
            add Transform(selected_avatar, xysize=(400, 358), fit="contain"):
                align (0.5, 0.5)
        else:
            text player["avatar"]:
                align (0.5, 0.5)
                size 32

    hbox:
        pos (314, 591)
        spacing 44

        for avatar_id, avatar_path in nyra_avatars.items():
            button:
                xysize (124, 124)
                padding (0, 0)
                background ("#77519CAA" if player["avatar"] == avatar_id else None)
                hover_background "#77519C88"
                action SetDict(player, "avatar", avatar_id)

                if renpy.loadable(avatar_path):
                    add Transform(avatar_path, xysize=(112, 112), fit="contain"):
                        align (0.5, 0.5)
                else:
                    text avatar_id:
                        align (0.5, 0.5)
                        size 22

    text _("Имя героини"):
        pos (540, 731)
        anchor (0.5, 0.5)
        size 26

    input:
        pos (270, 758)
        value DictInputValue(player, "name")
        length 20
        xysize (540, 52)
        size 30
        textalign 0.5

    textbutton "−":
        pos (332, 830)
        xysize (80, 68)
        text_color "#0000"
        text_hover_color "#0000"
        text_insensitive_color "#0000"
        hover_background "#FFFFFF22"
        sensitive player["age"] > 18
        action SetDict(player, "age", player["age"] - 1)

    text renpy.translate_string("Возраст") + " " + str(player["age"]):
        pos (540, 865)
        anchor (0.5, 0.5)
        size 30

    textbutton "+":
        pos (666, 830)
        xysize (80, 68)
        text_color "#0000"
        text_hover_color "#0000"
        text_insensitive_color "#0000"
        hover_background "#FFFFFF22"
        sensitive player["age"] < 42
        action SetDict(player, "age", player["age"] + 1)

    text _("Характеристики"):
        pos (1630, 148)
        anchor (0.5, 0.5)
        size 44

    text renpy.translate_string("Свободные очки: {}").format(player["free_points"]) + " / 6":
        pos (1598, 228)
        anchor (0.5, 0.5)
        size 34

    grid 2 4:
        pos (960, 295)
        transpose True
        xspacing 132
        yspacing 35

        for stat_key, stat_label in nyra_stat_labels:
            fixed:
                xysize (608, 82)

                text stat_label:
                    xpos 14
                    xsize 304
                    size 32
                    yalign 0.5

                textbutton "−":
                    xpos 318
                    xysize (72, 82)
                    text_size 38
                    text_align (0.5, 0.5)
                    text_color "#FFF1DA"
                    sensitive player["stats"][stat_key] > 5
                    action Function(change_nyra_stat, stat_key, -1)

                text str(player["stats"][stat_key]):
                    xpos 455
                    xanchor 0.5
                    size 36
                    yalign 0.5

                textbutton "+":
                    xpos 522
                    xysize (72, 82)
                    text_size 38
                    text_align (0.5, 0.5)
                    text_color "#FFF1DA"
                    sensitive player["free_points"] > 0
                    action Function(change_nyra_stat, stat_key, 1)

    hbox:
        pos (270, 952)
        spacing 120

        for category in talent_categories:
            $ category_key = category["key"]

            vbox:
                xsize 600

                textbutton category["name"]:
                    xysize (600, 48)
                    text_size 32
                    text_align (0.5, 0.5)
                    text_color "#FFF1DA"
                    action SetScreenVariable(
                        "open_category",
                        None if open_category == category_key else category_key
                    )

                if open_category == category_key:
                    for talent_id, talent_name in category["options"]:
                        textbutton talent_name:
                            xysize (600, 51)
                            text_size 30
                            text_align (0.5, 0.5)
                            text_color "#FFF1DA"
                            action [
                                SetDict(player["talents"], category_key, talent_id),
                                SetScreenVariable("open_category", None)
                            ]
                else:
                    textbutton get_talent_name(category, player["talents"][category_key]):
                        xysize (600, 120)
                        text_size 38
                        text_align (0.5, 0.5)
                        text_color "#FFF1DA"
                        action SetScreenVariable("open_category", category_key)

    textbutton _("Подтвердить персонажа"):
        pos (1280, 1251)
        anchor (0.5, 0.5)
        xysize (660, 88)
        text_size 38
        text_align (0.5, 0.5)
        text_color "#FFF1DA"
        text_insensitive_color "#C3BAD9"
        sensitive (
            player["free_points"] == 0
            and valid_nyra_name(player["name"])
        )
        action [
            SetDict(player, "name", player["name"].strip() or renpy.translate_string("Найра")),
            Return("confirmed")
        ]



translate english strings:

    old "Создание персонажа"
    new "Character Creation"

    old "Имя героини"
    new "Character Name"

    old "Если оставить поле пустым, будет использовано имя Найра."
    new "Leave the field empty to use the name Nyra."

    old "Возраст"
    new "Age"

    old "Характеристики"
    new "Stats"

    old "Свободные очки: {}"
    new "Points remaining: {}"

    old "Атака"
    new "Attack"

    old "Защита"
    new "Defense"

    old "Магическая атака"
    new "Magic Attack"

    old "Магическая защита"
    new "Magic Defense"

    old "Уклонение"
    new "Evasion"

    old "Скорость"
    new "Speed"

    old "Выносливость"
    new "Stamina"

    old "Магический запас"
    new "Mana"

    old "Выбор талантов"
    new "Talent Selection"

    old "Скрытность"
    new "Stealth"

    old "Тихий шаг"
    new "Silent Step"

    old "Быстрый рывок"
    new "Quick Dash"

    old "Невидимость"
    new "Invisibility"

    old "Физические навыки"
    new "Physical Skills"

    old "Урон"
    new "Damage"

    old "Ловкость"
    new "Agility"

    old "Кошачьи способности"
    new "Feline Abilities"

    old "Кошачий взгляд"
    new "Cat Vision"

    old "Острый слух"
    new "Keen Hearing"

    old "Кошачье чутьё"
    new "Feline Instinct"

    old "Подтвердить персонажа"
    new "Confirm Character"

    old "Найра"
    new "Nyra"
