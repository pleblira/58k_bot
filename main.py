from coinmarketcap_get_btc_usd import *
from tweet_with_apiv2 import *
import random
import urllib.request
import text_on_images
import subprocess
import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from text_on_images import *
# from sparkle_gif_create_frames import *
# from s3_update_LN_capacity_and_compare import *
import time
from post_note import *
from upload_to_voidcat_and_return_url import *

def bot58k():
    # fetching BTC price in USD
    btc_usd = coinmarketcap_get_btc_usd()
    btc_usd_text =f"BTC price: ${btc_usd:,.0f}"

    price_58k = btc_usd / 58000
    print(f"{price_58k:.3f}")

    text_on_images(f"{price_58k:.3f}", "58k_bot.png")
    tweet_with_apiv2("58k update\n\nnpub16f3vcd2tqkl3x72uxpzkcqudtjrt9mp5h7x69k4p802wptwh7qmqjeaq7t", "58k_bot_with_text.png")
    post_note(upload_to_voidcat_and_return_url("58k_bot_with_text.png", "png"))
    # upload_to_voidcat_and_return_url("58k_bot_with_text.png", "png")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(bot58k, 'cron', hour=12, minute=30, timezone="America/New_York")
    scheduler.start()
