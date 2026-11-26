#   ____  ____  _     ___ _____ ____  _   _    _    ____  ____    ____ _____ _   _ ____ ___ ___
#  / ___||  _ \| |   |_ _|_   _/ ___|| | | |  / \  |  _ \|  _ \  / ___|_   _| | | |  _ \_ _/ _ \
#  \___ \| |_) | |    | |  | | \___ \| |_| | / _ \ | |_) | | | | \___ \ | | | | | | | | | | | | |
#   ___) |  __/| |___ | |  | |  ___) |  _  |/ ___ \|  _ <| |_| |  ___) || | | |_| | |_| | | |_| |
#  |____/|_|   |_____|___| |_| |____/|_| |_/_/   \_\_| \_\____/  |____/ |_|  \___/|____/___\___/

# /* ******************************************************************************************************** */
# /*                                                                                                          */
# /*   File: C:\renpy\games\UnluckyDungeonAdventureAcademy\game\data\items.rpy                                */
# /*                                                        /\_/\                                             */
# /*                                                       ( •.• )                                            */
# /*   By: unluckydungeonadventure.gmail.com                > ^ <                                             */
# /*                                                                                                          */
# /*   Created: 2026/11/27 00:43:57 by UDA                                                                    */
# /*   Updated: 2026/11/27 00:43:57 by UDA                                                                    */
# /*                                                                                                          */
# /* ******************************************************************************************************** */


# game/data/items.rpy

# Общий каталог предметов.
define item_database = {
    "health_potion": {
        "name": _("Зелье здоровья"),
        "description": _("Восстанавливает 50 HP."),
        "type": "consumable",
        "max_stack": 20,

        "icons": {
            "small": "images/items/small/health_potion.png",
            "medium": "images/items/medium/health_potion.png",
            "large": "images/items/large/health_potion.png"
        }
    },

    "academy_key": {
        "name": _("Ключ академии"),
        "description": _("Ключ от одной из комнат академии."),
        "type": "quest",
        "max_stack": 1,

        "icons": {
            "small": "images/items/small/academy_key.png",
            "medium": "images/items/medium/academy_key.png",
            "large": "images/items/large/academy_key.png"
        }
    },

    "mana_potion": {
        "name": _("Зелье маны"),
        "description": _("Восстанавливает 30 MP."),
        "type": "consumable",
        "max_stack": 20,

        "icons": {
            "small": "images/items/small/mana_potion.png",
            "medium": "images/items/medium/mana_potion.png",
            "large": "images/items/large/mana_potion.png"
        }
    }
}
