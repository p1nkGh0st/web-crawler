# utils.py
"""
Utility functions for scraping data, saving Excel reports, and sending discord notifier.
"""

import requests
from datetime import datetime
import csv
import config


def get_crypto_prices_and_save():
    """
    Fetches real-time price data for BTC, ETH, and XRP via CoinGecko API,
    appends the data into a cumulative CSV log, and returns a formatted report string.
    """
    try:
        # 1. Fetch JSON data from CoinGecko API
        response = requests.get(config.CRYPTO_URL)
        data = response.json()  # Convert the fetched data into a Python dictionary immediately
        
        # 2. Parse the data
        btc_price = data['bitcoin']['usd']
        btc_change = data['bitcoin']['usd_24h_change']
        
        eth_price = data['ethereum']['usd']
        eth_change = data['ethereum']['usd_24h_change']
        
        xrp_price = data['ripple']['usd']
        xrp_change = data['ripple']['usd_24h_change']
        
        # 3. Build the report string
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        report = f"🪙 **[Crypto Real-Time Market Report]** ({current_time})\n"
        report += "-" * 40 + "\n"
        report += f"• **Bitcoin (BTC):** ${btc_price:,} ({btc_change:+.2f}%)\n"
        report += f"• **Ethereum (ETH):** ${eth_price:,} ({eth_change:+.2f}%)\n"
        report += f"• **Ripple (XRP):** ${xrp_price:.4f} ({xrp_change:+.2f}%)\n"
        report += "-" * 40 + "\n"
        
        # 4. Save to CSV log
        filename = "crypto_price_history.csv"
        
        # Check if the file already exists to decide whether to write the header
        import os
        file_exists = os.path.isfile(filename)
        
        # Open in 'append' mode to store data cumulatively without overwriting
        with open(filename, mode="a", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                # Write the header only if the file is being created for the first time
                writer.writerow(["Timestamp", "Coin", "Price (USD)", "24h Change (%)"])
                
            # Log data for each coin row by row
            writer.writerow([current_time, "BTC", btc_price, f"{btc_change:.2f}"])
            writer.writerow([current_time, "ETH", eth_price, f"{eth_change:.2f}"])
            writer.writerow([current_time, "XRP", xrp_price, f"{xrp_change:.2f}"])
            
        print(f"💾 [SUCCESS] Market data successfully logged into: {filename}")
        return report

    except Exception as e:
        return f"❌ Error fetching crypto market data: {e}\n"


def send_discord_notification(message):
    data = {"content": message}
    response = requests.post(config.DISCORD_WEBHOOK_URL, json=data)
    return response.status_code == 204
