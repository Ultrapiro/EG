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
    LEGEND_STRING = "1BVtsOKYBu2gh5qreovqHJT92_P1wxWcHmfDgDRG4uLeaNxAteyfnD5adQ2tSYVleKBEmFeBLLS3V65mFfHeAb3b8GTunWOorYM0xn0z0oAfBGqK2S-tZpiT-ez3mpik2wUeDG1AWWQCw-ft3d3J4tX-5wj-CMJNibdCDnoyFFsMYufhC7u8VUJESHow0GRReqWZ0rFWL-YRIfiMUYwfevQqr6CfLh4lOodcUxqAPvNWsDivg1W1K28org5qKsfiN2sEUstrXsogNMrgxUUKlNguKCbsWQfpo6b6WVG2o_wpv5Xnn2zjyneFHnYJl0aJrq6RujWpzEKhnCZ0LXW0LGSm9MCkHwDM="
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
