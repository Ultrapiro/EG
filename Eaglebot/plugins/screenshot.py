import io
import traceback
from datetime import datetime

import requests
from selenium import webdriver
from validators.url import url

from Eaglebot import eagle

from ..Config import Config
from ..core.managers import eor
from . import reply_id

menu_category = "utils"


@eagle.eagle_cmd(
    pattern="(ss|gis) ([\s\S]*)",
    command=("ss", menu_category),
    info={
        "header": "To Take a screenshot of a website.",
        "usage": "{tr}ss <link>",
        "examples": "{tr}ss https://github.com/Badhacker98/EAGLEBOT",
    },
)
async def _(event):
    "To Take a screenshot of a website."
    if Config.CHROME_BIN is None:
        return await eor(event, "Need to install Google Chrome. Module Stopping.")
    eagleevent = await eor(event, "`Processing ...`")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN
        await event.edit("`Starting Google Chrome BIN`")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        cmd = event.pattern_match.group(1)
        input_str = event.pattern_match.group(2)
        inputstr = input_str
        if cmd == "ss":
            eagleurl = url(inputstr)
            if not eagleurl:
                inputstr = "http://" + input_str
                eagleurl = url(inputstr)
            if not eagleurl:
                return await eagleevent.edit("`The given input is not supported url`")
        if cmd == "gis":
            inputstr = f"https://www.google.com/search?q={input_str}"
        driver.get(inputstr)
        await eagleevent.edit("`Calculating Page Dimensions`")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await eagleevent.edit("`Stoppping Chrome Bin`")
        driver.close()
        message_id = await reply_id(event)
        end = datetime.now()
        ms = (end - start).seconds
        hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
        await eagleevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = input_str + ".PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=hmm,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await eagleevent.edit(f"`{traceback.format_exc()}`")


@eagle.eagle_cmd(
    pattern="scapture ([\s\S]*)",
    command=("scapture", menu_category),
    info={
        "header": "To Take a screenshot of a website.",
        "description": "For functioning of this command you need to set SCREEN_SHOT_LAYER_ACCESS_KEY var",
        "usage": "{tr}scapture <link>",
        "examples": "{tr}scapture https://github.com/Badhacker98/EAGLEBOT",
    },
)
async def _(event):
    "To Take a screenshot of a website."
    start = datetime.now()
    message_id = await reply_id(event)
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        return await eor(
            event,
            "`Need to get an API key from https://screenshotlayer.com/product and need to set it SCREEN_SHOT_LAYER_ACCESS_KEY !`",
        )
    eagleevent = await eor(event, "`Processing ...`")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    inputstr = input_str
    eagleurl = url(inputstr)
    if not eagleurl:
        inputstr = f"http://{input_str}"
        eagleurl = url(inputstr)
    if not eagleurl:
        return await eagleevent.edit("`The given input is not supported url`")
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, inputstr, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    end = datetime.now()
    ms = (end - start).seconds
    hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=hmm,
                    force_document=True,
                    reply_to=message_id,
                )
                await eagleevent.delete()
            except Exception as e:
                await eagleevent.edit(str(e))
    else:
        await eagleevent.edit(f"`{response_api.text}`")
