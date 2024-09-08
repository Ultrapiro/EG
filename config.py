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
    EAGLE_STRING = "1BVtsOIIBu63krgyOCV-iHfwYI8Eo9VX7N2KYDCVgucf8m9GN2exTobLSwgi2OSrlXMXhQtUY0u9DtKFoUl934nFlbArRZ3SLRIQWhtKRC_PSAu7d4d4d5geO2nUhIik3D0La3fZrJ6ySSDXUM8BPlkPygZVCJ17FBM1daYpOqPvd3teNzQdJd3WpqM33tT3mwqez3T4mdryVgR4eD8PRBygmUJMGcgg--fb_TfOxHvqoIZOKzLMQ-5Lr33SMdFp8cYyX_v4EhFqWzXLUdyYwl8J6wWZJopw5mDdfhWvuKfpb8vGz_SvZQL0NJveBK8QT15Yl35bCSRJrjUEKFjOtCyvWU_WHpdM="
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
