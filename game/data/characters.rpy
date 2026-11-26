#   ____  ____  _     ___ _____ ____  _   _    _    ____  ____    ____ _____ _   _ ____ ___ ___
#  / ___||  _ \| |   |_ _|_   _/ ___|| | | |  / \  |  _ \|  _ \  / ___|_   _| | | |  _ \_ _/ _ \
#  \___ \| |_) | |    | |  | | \___ \| |_| | / _ \ | |_) | | | | \___ \ | | | | | | | | | | | | |
#   ___) |  __/| |___ | |  | |  ___) |  _  |/ ___ \|  _ <| |_| |  ___) || | | |_| | |_| | | |_| |
#  |____/|_|   |_____|___| |_| |____/|_| |_/_/   \_\_| \_\____/  |____/ |_|  \___/|____/___\___/

# /* ******************************************************************************************************** */
# /*                                                                                                          */
# /*   File: C:\renpy\games\UnluckyDungeonAdventureAcademy\game\data\characters.rpy                           */
# /*                                                        /\_/\                                             */
# /*                                                       ( •.• )                                            */
# /*   By: unluckydungeonadventure.gmail.com                > ^ <                                             */
# /*                                                                                                          */
# /*   Created: 2026/11/26 23:16:53 by UDA                                                                    */
# /*   Updated: 2026/11/26 23:16:53 by UDA                                                                    */
# /*                                                                                                          */
# /* ******************************************************************************************************** */


# Доступные аватары Nyra.
define nyra_avatars = {
    "nyra_01": "images/characters/nyra/avatars/nyra_01.png",
    "nyra_02": "images/characters/nyra/avatars/nyra_02.png",
    "nyra_03": "images/characters/nyra/avatars/nyra_03.png"
}

# Каталог персонажей.
define game_characters = {
    "nyra": {
        "name": _("Найра"),
        "avatars": [
            "nyra_01",
            "nyra_02",
            "nyra_03"
        ],
        "sprite_folder": "images/characters/nyra/sprites/"
    }
}


# Категории и доступные таланты.
define talent_categories = [
    {
        "key": "stealth",
        "name": _("Скрытность"),
        "options": [
            ("silent_step", _("Тихий шаг")),
            ("quick_dash", _("Быстрый рывок")),
            ("invisibility", _("Невидимость"))
        ]
    },
    {
        "key": "physical",
        "name": _("Физические навыки"),
        "options": [
            ("damage", _("Урон")),
            ("dodge", _("Уклонение")),
            ("agility", _("Ловкость"))
        ]
    },
    {
        "key": "cat",
        "name": _("Кошачьи способности"),
        "options": [
            ("cat_vision", _("Кошачий взгляд")),
            ("hearing", _("Острый слух")),
            ("instinct", _("Кошачье чутьё"))
        ]
    }
]


# Функция получения названия таланта
init python:

    def get_talent_name(category, talent_id):
        for option_id, name in category["options"]:
            if option_id == talent_id:
                return name

        return talent_id