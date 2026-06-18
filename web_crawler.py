import requests
from bs4 import BeautifulSoup
from datetime import datetime


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

        print("☀️ Today's Weather Summary (Los Angeles)")
        print(f"- {weather_text}")
        print("-" * 40)
    except Exception as e:
        print(f"❌ Error fetching weather data: {e}")


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

        print("📰 Today's Google Entertainment Headlines")

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
            print(f"{idx}. {title}")

        print("-" * 40)
    except Exception as e:
        print(f"❌ Error fetching news headlines: {e}")


if __name__ == "__main__":
    print(f"=== ⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')} Briefing Started ===")
    print("-" * 40)
    get_weather()
    get_news_headlines()
