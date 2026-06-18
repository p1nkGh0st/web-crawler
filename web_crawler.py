import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import schedule  
import time

def get_weather():
    """Fetches real-time weather info for Los Angeles via wttr.in."""
    url = "https://wttr.in/Los+Angeles?format=3"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers)

        # 1. Split the raw text response by newline characters into a list of lines
        lines = response.text.split("\n")

        # 2. Loop through the lines to filter for the one containing "Los Angeles:"
        weather_text = "N/A"
        for line in lines:
            if "Los Angeles:" in line:
                # 3. Clean up any leftover HTML tags (like <div>) to get pure text
                weather_text = BeautifulSoup(line, "html.parser").get_text().strip()
                break

        # Format the weather block as a string
        weather_report = "☀️ Today's Weather Summary (Los Angeles)\n"
        weather_report += f"- {weather_text}\n"
        weather_report += "-" * 40 + "\n"
        return weather_report
    except Exception as e:
        return f"❌ Error fetching weather data: {e}\n"


def get_news_headlines():
    """Fetches top 5 entertainment headlines from Google News."""
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"  # 엔터 섹션
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all potential headline anchor tags
        raw_headlines = soup.find_all("a", attrs={"data-n-tid": True})
        if not raw_headlines:
            raw_headlines = [
                a for a in soup.select("article a") if len(a.get_text(strip=True)) > 15
            ]

        news_report = "📰 Today's Google Entertainment Headlines\n"

        # 👈 Use a set or list check to filter out duplicate titles
        unique_titles = []

        # Initialize a set to store unique keywords from processed headlines
        seen_keywords = set()

        for title in raw_headlines:
            clean_title = title.get_text(strip=True)

            if clean_title and clean_title not in unique_titles:
                # Split the headline into lowercase individual words
                words = clean_title.lower().split()

                # Extract core keywords (words longer than 3 chars, excluding common stop words)
                keywords = {
                    w
                    for w in words
                    if len(w) > 3 and w not in ["from", "with", "that", "this", "after"]
                }

                # Check for overlapping keywords with previously processed headlines
                if keywords & seen_keywords:
                    continue  # Skip this headline if it covers the same topic

                # Save the headline only if it's a completely unique topic
                unique_titles.append(clean_title)
                seen_keywords.update(keywords)  # Add new keywords to the tracked set

            if len(unique_titles) == 5:
                break

        for idx, title in enumerate(unique_titles, 1):
            news_report += f"{idx}. {title}\n"

        news_report += "-" * 40 + "\n"
        return news_report
    except Exception as e:
        return f"❌ Error fetching news headlines: {e}\n"


def send_email_notification(content):
    """Sends the compiled briefing content directly to your Gmail inbox."""
    # ⚠️ CRITICAL: Replace these placeholders with your actual email and 16-digit app password
    sender_email = "your_email@gmail.com"
    app_password = "xxxxxxxxxxxxxxxx"  # Put your 16-digit key here without spaces
    receiver_email = "your_email@gmail.com"
    
    # Setup secure SSL connection with Gmail's SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    
    # Construct the email packet
    today_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = f"☕ Daily Briefing Report ({today_str})"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    
    try:
        # Establish a secure connection and login
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("🚀 Briefing email has been successfully delivered to your inbox!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


def run_daily_briefing():
    """The core run_daily_briefing that compiles data and sends the briefing email."""
    print(f"\n=== ⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')} Briefing Started ===")
    print("-" * 40)
    
    # 1. Compile all fetched data into a single content block
    briefing_content = f"=== ⏰ Morning Briefing ===\n\n"
    briefing_content += get_weather()
    briefing_content += get_news_headlines()
    
    # 2. Print to terminal and shoot the email
    print(briefing_content)
    send_email_notification(briefing_content)
    print("=== 😴 run_daily_briefing Finished. Returning to standby mode ===")


if __name__ == "__main__":
    print("⚡ Daily Briefing Daemon Service is now running...")
    print("🕒 Standing by for the scheduled time...")
    
    # 👈 Test Rule: Runs the run_daily_briefing immediately once upon starting to verify it works
    run_daily_briefing()
    
    # Schedule Rule: Set it to run every single day at 08:30 AM
    # (You can change "08:30" to any time you want to test, e.g., 2 minutes from now)
    schedule.every().day.at("08:30").do(run_daily_briefing)
    
    # Infinite loop to keep the script alive and checking the clock
    while True:
        schedule.run_pending()  # Check if there is a scheduled run_daily_briefing to run
        time.sleep(1)       # Sleep for 1 second to prevent high CPU usage

   
