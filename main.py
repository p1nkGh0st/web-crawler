# main.py
"""
Main entry point for the Automated Daily Briefing Service.
"""

import schedule
import time
from datetime import datetime
import config
import utils


def run_daily_briefing():
    """The core coordination job that compiles crypto data and triggers notifications."""
    print(f"\n=== ⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')} Crypto Monitoring Started ===")
    print("-" * 40)

    # 1. Compile data blocks from utils
    briefing_content = f"===⏰ Crypto Market Briefing ===\n\n"
    briefing_content += utils.get_crypto_prices_and_save()

    # 2. Print summary and send out the Discord notification
    print(briefing_content)
    utils.send_discord_notification(briefing_content)
    print("=== 😴 Job Finished. Returning to standby mode ===")


if __name__ == "__main__":
    print("⚡ Automated Crypto Monitor Service is now running...")
    print(f"🕒 Standby mode activated. Scheduled time: {config.SCHEDULED_TIME}")

    # Test Rule: Run immediately once upon startup to verify system status
    run_daily_briefing()

    # Schedule Rule: Automated trigger from config setting
    schedule.every().day.at(config.SCHEDULED_TIME).do(run_daily_briefing)

    # 24hr Infinite loop
    while True:
        schedule.run_pending()
        time.sleep(60)
