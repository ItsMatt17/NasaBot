import os
from dotenv import load_dotenv
from typing import List
import logging


logging.basicConfig(encoding='utf-8', level=logging.INFO)




load_dotenv()
DISCORD_AUTH = os.environ["DISCORD_AUTH"]
