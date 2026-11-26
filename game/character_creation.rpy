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



screen create_nyra():

    modal True

    default open_category = None

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1900
        ysize 1250
        padding (50, 40)

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 25

                text _("Создание персонажа"):
                    size 52

                # Выбор аватара.
                text _("Выберите аватар"):
                    size 36

                hbox:
                    spacing 20

                    for avatar_id, avatar_path in nyra_avatars.items():

                        button:
                            xsize 200
                            ysize 210

                            background (
                                "#77519C"
                                if player["avatar"] == avatar_id
                                else "#35254C"
                            )

                            action SetDict(
                                player, "avatar", avatar_id
                            )

                            vbox:
                                xalign 0.5
                                spacing 5

                                if renpy.loadable(avatar_path):
                                    add avatar_path:
                                        xsize 150
                                        ysize 150
                                else:
                                    text avatar_id:
                                        size 22

                                text avatar_id:
                                    size 20

                # Имя персонажа.
                text _("Имя героини"):
                    size 36

                input:
                    value DictInputValue(player, "name")
                    length 20
                    xsize 650

                text _("Если оставить поле пустым, будет использовано имя Найра."):
                    size 22

                # Возраст.
                text _("Возраст"):
                    size 36

                hbox:
                    spacing 30

                    textbutton "−":
                        sensitive player["age"] > 1
                        action SetDict(
                            player, "age",
                            player["age"] - 1
                        )

                    text str(player["age"]):
                        size 32

                    textbutton "+":
                        sensitive player["age"] < 120
                        action SetDict(
                            player, "age",
                            player["age"] + 1
                        )

                # Характеристики.
                text _("Распределение характеристик"):
                    size 36

                text _("Свободные очки: {}").format(
                    player["free_points"]
                ):
                    size 30

                for stat_key, stat_label in nyra_stat_labels:

                    hbox:
                        spacing 20

                        text stat_label:
                            xsize 420
                            size 28

                        textbutton "−":
                            sensitive player["stats"][stat_key] > 5
                            action Function(
                                change_nyra_stat,
                                stat_key, -1
                            )

                        text str(player["stats"][stat_key]):
                            size 30
                            xminimum 50
                            text_align 0.5

                        textbutton "+":
                            sensitive player["free_points"] > 0
                            action Function(
                                change_nyra_stat,
                                stat_key, 1
                            )

                # Выбор талантов.
                text _("Выбор талантов"):
                    size 36

                for category in talent_categories:

                    $ category_key = category["key"]

                    vbox:
                        spacing 10

                        text category["name"]:
                            size 28

                        textbutton get_talent_name(
                            category,
                            player["talents"][category_key]
                        ):
                            action SetScreenVariable(
                                "open_category",
                                (
                                    None
                                    if open_category == category_key
                                    else category_key
                                )
                            )

                        if open_category == category_key:

                            for talent_id, talent_name in category["options"]:

                                textbutton talent_name:
                                    action [
                                        SetDict(
                                            player["talents"],
                                            category_key,
                                            talent_id
                                        ),
                                        SetScreenVariable(
                                            "open_category",
                                            None
                                        )
                                    ]

                # Завершение создания.
                textbutton _("Подтвердить персонажа"):
                    xalign 0.5

                    sensitive player["free_points"] == 0

                    action [
                        SetDict(player, "name", player["name"].strip() or _("Найра")),
                        Return("confirmed")
                    ]
