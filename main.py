# main.py
"""
Utility script for manual data check.
"""

from datetime import datetime
import utils

def run_manual_check():
    """Manually trigger one-time crypto data fetch and notification."""
    print(f"\n=== 🔍 Manual Check Started: {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    
    # utils.get_crypto_prices_and_save returns two values 
    _, report = utils.get_crypto_prices_and_save()

    # Send report to Discord.
    utils.send_discord_notification(report)
    print("=== ✅ Manual Job Finished ===")

if __name__ == "__main__":
    run_manual_check()
