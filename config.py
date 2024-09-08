# CHANGE TO NAME CUT THE (VPS_) ONLY config.py 

from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25742938
    API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
    # the name to display in your alive message
    ALIVE_NAME = "♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://lwktrpsc:1UlTfWHhnxKZWRETlLu6AF0x4AsyKXhO@rosie.db.elephantsql.com/lwktrpsc"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    EAGLE_STRING = "1BVtsOL8Bu44ddMvJXGn5vhO-vULQMK3lkmLRhto3OyQ14Rafyr4gJCJPC9uOExoFdp6HntVG3U-J16jJTsfHgTLZKR_8zQP_ePttAY_KrsqNoOgXX9BJTJztV3fOfSmw4DpwUXNXTG-BaFrIbFon8ShgYyggPSFmVL8ZQrFIVquVmEnqjVJoFtN3L3jrs3LEmE89XY9klDknFUOxxnSGXhHu15mbA0BfClGNl3ZlK_Ze_MUd4sNCtY0bLQWYAa3AaVV1v1NgmbZ3Xzls1mdXdfSNdTr8wYPa90nJCZICP5nrt3J3Ml2CFruWtrh2gP9h8xeGcwXy_U0yWjVQ6LHnXAz_9Wvw7oY="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "7451378287:AAHmSqw8cIDKo4UmImAK2opVQkZIm4ArXjg"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "Bad"
    UPSTREAM_REPO = "Bad"
    VCMODE = False
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
