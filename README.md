# 🪙 Crypto Market Monitor & Discord Alert Bot

A modularized, automated Python service that tracks real-time cryptocurrency prices, logs data to CSV, provides a web-based dashboard, and delivers scheduled market updates to your Discord channel.

## 🚀 Features
- **Real-time Crypto Tracking:** Fetches live market data including current price and 24h percentage change for major coins (BTC, ETH, XRP) via CoinGecko API.
- **Web Dashboard:** Interactive UI powered by Streamlit to view market data and trigger manual checks instantly.
- **Automated Data Archiving:** Archives market data into crypto_price_history.csv for long-term historical analysis.
- **Scheduled Discord Alerts:** Automates market updates by delivering price summaries to your Discord channel at your predefined schedule.
- **24/7 Automation Scheduler:** Operates in standby mode, triggering the monitoring job automatically at your custom schedule via a robust scheduling engine.
- **Modular Architecture:** Separated logic for automation (scheduler) and UI (Streamlit) to ensure system stability and independent operation.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Libraries Used:** 
  - `requests` (for API interaction & Discord webhook delivery)
  - `schedule` (for automated task scheduling)
  - `streamlit` (Web dashboard UI)

## 💻 How to Run

Follow these steps to set up and run the service locally:

### 1. Clone the repository

```bash
git clone https://github.com/p1nkGh0st/web-crawler.git

```

### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your Discord Webhook URL:

```text
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your-id/your-token

```

### 4. Run the components

**To start the Discord Bot Scheduler:**

```bash
python3 scheduler.py

```

**To start the Web Dashboard:**

```bash
streamlit run app.py

```

