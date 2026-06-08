import collections
import re
import requests
from bs4 import BeautifulSoup

# Define the URL and headers to simulate a legitimate browser request
URL = "https://www.newsnow.co.uk/h/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_top_headlines(url):
    print(f"Fetching headlines from {url}...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # NewsNow anchors containing headlines typically have the class 'hll'
    headline_elements = soup.find_all("a", class_="hll")

    headlines = []
    for el in headline_elements:
        text = el.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines


def generate_word_summary(headlines, top_n=15):
    if not headlines:
        print("No headlines found to analyze.")
        return

    # Combined text from all headlines
    all_text = " ".join(headlines).lower()

    # Use regex to find words (ignoring punctuation)
    words = re.findall(r"\b\w+\b", all_text)

    # A common list of "stop words" to filter out from the frequency breakdown
    stop_words = {
        "the",
        "to",
        "and",
        "a",
        "in",
        "of",
        "for",
        "on",
        "is",
        "at",
        "with",
        "by",
        "as",
        "from",
        "it",
        "that",
        "this",
        "after",
        "over",
        "new",
        "says",
        "will",
        "are",
        "be",
        "us",
        "uk",
        "i",
        "you",
        "he",
        "she",
        "has",
        "have",
        "was",
    }

    filtered_words = [word for word in words if word not in stop_words]

    # Count frequencies
    word_counts = collections.Counter(filtered_words)
    most_common = word_counts.most_common(top_n)

    # Print Summary Report
    print("\n" + "=" * 40)
    print(f"SUMMARY OF TOP HEADLINES")
    print("=" * 40)
    print(f"Total Headlines Analyzed: {len(headlines)}")
    print(f"Total Meaningful Words Extracted: {len(filtered_words)}")
    print("-" * 40)
    print(f"Top {top_n} Most Frequently Occurring Words:")
    print("-" * 40)

    for word, count in most_common:
        print(f"• {word:<15} : {count} occurrences")
    print("=" * 40)


if __name__ == "__main__":
    headlines = get_top_headlines(URL)

    # Show a preview of the scraped headlines
    if headlines:
        print(f"Successfully scraped {len(headlines)} headlines.")
        print("\nPreview of top 5 headlines:")
        for idx, headline in enumerate(headlines[:5], 1):
            print(f"{idx}. {headline}")

        # Generate and display the word frequency summary
        generate_word_summary(headlines)
