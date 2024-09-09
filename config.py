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
    EAGLE_STRING = "1BVtsOKYBu0QNNt8J_i82v2GiDBVPUCS3owzDzIjmJ92GKuH2TBXsRFH77E2C8uRDrOgAKLweybxYWTm8yaibdahG1fhVxmc-iDR5q-Yatz8Us1tU-EimyjrL3Jx_0ad6GHa8j5iXpuvWtfr5JhvVv_l-NRbqlmgaRCAK8ifB9UmhjRxSZLD9Dxhc5zsNx-4Bhkb2lui_HAhPbZxIyqfjYdEOFAa_RDzp9jUvSa4XQkZmjfxOBZZMDKlHvI_rrMaMBt59Z096o1OoqSkPOiqxwEs9IUSUwZTOz4Eb53gfDFu4Ug9gp4d2BWibxSXy3w6sbT_w4mqnP7iaSgkVwffeC7Bnc2yV8Xg="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "7217412726:AAEsahhAS5Li1w1DIVccJAVeqo69jANZMoM"
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
    LOGGER_ID = -1002381417478
    PRIVATE_GROUP_BOT_API_ID = -1002381417478
    EXTERNAL_REPO = "https://github.com/badmunda98/EaglePlugins"
    # if you need badcat plugins set "True"
