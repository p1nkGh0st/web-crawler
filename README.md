# 🌤️ Daily Briefing Web Crawler

A lightweight Python-based web crawler that fetches a real-time weather summary and the latest entertainment headlines to help you start your day with a quick briefing.

## 🚀 Features
- **Real-time Weather Summary:** Fetches current weather info for Los Angeles in a clean, plain-text format using `wttr.in`.
- **Google News Headlines:** Scrapes the top 5 entertainment headlines using `BeautifulSoup`.
- **Smart Topic Filtering:** Implements an advanced keyword-based de-duplication mechanism to filter out overlapping articles and ensure 5 unique news topics.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Libraries Used:** - `requests` (for handling HTTP requests)
  - `beautifulsoup4` (for parsing HTML content)

## 💻 How to Run
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
3. Run the web crawler script:
   ```bash
   python web_crawler.py

## 💻 Future Roadmaps (Level-Up Features)
[ ] Automation Scheduler: Automate the script to run daily at a specific time using the schedule library.

[ ] Email Notifications: Deliver the formatted daily briefing straight to your inbox via Python's smtplib.