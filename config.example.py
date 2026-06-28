# config.example.py
"""
[Template] Configuration settings for the Daily Briefing Web Crawler.
Instructions: Copy this file, rename it to 'config.py', and fill in your details.
"""

# Discord Webhook URLs
DISCORD_WEBHOOK_URL = "XXXXXXXXXXXXXXXXXXX" # Replace with your discord webhook URL

# Crypto API endpoint for BTC, ETH, and XRP price and 24h change data
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd&include_24hr_change=true"

# Scheduler Settings (Default)
SCHEDULED_TIME = "10:00"