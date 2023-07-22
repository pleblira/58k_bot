from coinmarketcap_get_btc_usd import *
from tweet_with_apiv2 import *
from apscheduler.schedulers.blocking import BlockingScheduler
from text_on_images import *
from post_note import *
from upload_to_voidcat_and_return_url import *

def bot58k():
    # fetching BTC price in USD
    btc_usd = coinmarketcap_get_btc_usd()

    price_58k = btc_usd / 58000
    print(f"{price_58k:.3f}")

    text_on_images(f"{price_58k:.4f}", "58k_bot.png")
    tweet_with_apiv2("58k update\n\nnpub16f3vcd2tqkl3x72uxpzkcqudtjrt9mp5h7x69k4p802wptwh7qmqjeaq7t", "58k_bot_with_text.png")
    post_note(upload_to_voidcat_and_return_url("58k_bot_with_text.png", "png"))

if __name__ == '__main__':
    bot58k()
    scheduler = BlockingScheduler()
    scheduler.add_job(bot58k, 'cron', hour=12, minute=30, timezone="America/New_York")
    scheduler.add_job(bot58k, 'cron', hour=00, minute=30, timezone="America/New_York")
    print("starting scheduler")
    scheduler.start()