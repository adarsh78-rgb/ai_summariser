import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')
        content = ' '.join([para.get_text() for para in paragraphs])
        return content.strip()
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
