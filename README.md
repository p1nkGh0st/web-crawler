# 🪙 Crypto Market Monitor & Discord Alert Bot

A lightweight, automated Python service that tracks real-time cryptocurrency prices (BTC, ETH, XRP), archives market data into a CSV log, and delivers instant price updates to your Discord channel.

## 🚀 Features
- **Real-time Crypto Tracking:** Fetches live market data including current price and 24h percentage change for major coins (BTC, ETH, XRP) via CoinGecko API.
- **Automated Data Archiving:** Automatically appends every fetch cycle's data into a timestamped, cumulative CSV log (`crypto_price_history.csv`) for historical price tracking.
- **Instant Discord Integration:** Delivers real-time market updates directly to your Discord channel using an Inbound Webhook.
- **24/7 Automation Scheduler:** Operates in standby mode, triggering the monitoring job automatically at your custom schedule via a robust scheduling engine.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Libraries Used:** - `requests` (for API interaction & Discord webhook delivery)
  - `schedule` (for automated task scheduling)

## 💻 How to Run
1. Clone this repository.
2. Install the required external dependencies:
   ```bash
   pip install requests schedule