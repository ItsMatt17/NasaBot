from dotenv import load_dotenv
import requests
import json
import os
from discord import Embed
from Utils.embeds import failed_embed_photo
from typing import Union
import logging


def authKey():
    """Checks if auth key is present in .env
    :return: str API KEY
    """
    load_dotenv()
    API_KEY = os.environ["API_KEY"]

    try:
        API_KEY = os.environ["API_KEY"]
        return API_KEY
    except KeyError as e:
        print(e)


API_KEY = authKey()


def get_photo():
    re = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")
    res = re.json()
    return res["url"], res["title"], res["explanation"]


def get_dated_photo(
    date: str,
) -> Union[tuple[str, str, str], None, str]:  # YYYY-MM-DD  Must be after 1995-06-16
    re = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}"
    )

    res = re.json()

    print(res)
    print(re.status_code)

    if re.status_code == 200:
        logging.info("Status Code 200")
        if len(res["explanation"]) > 1024:
            logging.critical("Message over char limit ")
            return "Limit"
        return (res["url"], res["title"], res["explanation"])
    else:
        logging.error(msg="Improper Status Code")
        return None
