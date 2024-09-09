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
    EAGLE_STRING = "1BVtsOKYBuyhduVwkleW2OHA7wH9R-VxlKJiIp8_f7PLWvv_j5FhaBbvcmOXcAljuK5E2IC7Q7tsex29DpLEY11E3gNSnUiKsGintKNlvQbqFjEvh4eq_ob6YQq23SLsMGpkT8M6lcmsBCQ4jh1C_V-BqItIOHmCBGodOqx0DFO8HVQms-4t4_D_YcXaHwPFFQjYNZHV0uEaJypCDsCuAwuHgFR30knXzn731wnVJkQTvRR0Be5M3PGxcF4OinxnM_gOHIjzVd0e3k1QGktLJ6fpGLipB9B3UFnC0kiCcmopB7cC7Y9cIiNQwArGUxu3Msth2a6V0rnNe6F5Vu07bavtP2wMtan0="
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
    RANDOM_STUFF_API_KEY = "20240908-1401-4740-801f-0d56de118901"
    LOGGER_ID = -1002355928218
    EXTERNAL_REPO = "https://github.com/badmunda98/EaglePlugins"
    # if you need badcat plugins set "True"
