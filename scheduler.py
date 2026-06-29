# scheduler.py
import schedule
import time
import config
import utils

def daily_update():
    # Retrieve current market data and a formatted report
    _, report = utils.get_crypto_prices_and_save()

    # Send the update to the connected Discord channel
    utils.send_discord_notification(report)
    print("Daily market update has been successfully delivered!")

# Set the automated task to trigger daily at the time configured in config.py
schedule.every().day.at(config.SCHEDULED_TIME).do(daily_update)

# Infinite loop to keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)