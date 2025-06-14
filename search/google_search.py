# import requests
# from bs4 import BeautifulSoup

# def google_search(query, num_results=5):
#     url = f"https://html.duckduckgo.com/html/?q={query}"
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers=headers)

#     soup = BeautifulSoup(response.text, "html.parser")
#     links = []

#     for a in soup.find_all("a", {"class": "result__a"}):
#         href = a.get("href")
#         if href:
#             links.append(href)
#         if len(links) >= num_results:
#             break

#     return links

# print(google_search("India"))





# import os
# import requests
# import urllib.parse
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv

# # Load env variables
# load_dotenv()
# SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# # -------- SERPAPI METHOD --------
# def google_search_serpapi(query, num_results=5):
#     try:
#         from serpapi import GoogleSearch
#     except ModuleNotFoundError:
#         print("Please install serpapi: pip install google-search-results")
#         return []

#     if not SERPAPI_KEY:
#         print("SERPAPI_KEY not found in environment variables.")
#         return []

#     search = GoogleSearch({
#         "q": query,
#         "api_key": SERPAPI_KEY,
#         "num": num_results
#     })
#     results = search.get_dict()
#     links = [res['link'] for res in results.get("organic_results", []) if 'link' in res]
#     return links

# # -------- FREE SCRAPING METHOD --------
# def google_search_scraper(query, num_results=5):
#     query = urllib.parse.quote_plus(query)
#     url = f"https://www.google.com/search?q={query}"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }

#     try:
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#     except Exception as e:
#         print(f"Error accessing Google: {e}")
#         return []

#     soup = BeautifulSoup(response.text, "html.parser")
#     search_results = []

#     for g in soup.find_all('div', class_='tF2Cxc'):
#         link_tag = g.find('a')
#         if link_tag and link_tag['href']:
#             search_results.append(link_tag['href'])
#             if len(search_results) >= num_results:
#                 break

#     return search_results

# # -------- Universal Function --------
# def google_search(query, num_results=5, use_serpapi=True):
#     if use_serpapi:
#         return google_search_serpapi(query, num_results)
#     else:
#         return google_search_scraper(query, num_results)






from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def google_search(query, num_results=5):
    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results
    })
    results = search.get_dict()
    links = []

    for res in results.get("organic_results", []):
        if 'link' in res:
            links.append(res['link'])
    return links


# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# def google_search(query, num_results=5):
#     query = urllib.parse.quote_plus(query)
#     url = f"https://www.google.com/search?q={query}"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print("Failed to retrieve search results.")
#         return []

#     soup = BeautifulSoup(response.text, "html.parser")
#     search_results = []

#     for g in soup.find_all('div', class_='tF2Cxc'):
#         link_tag = g.find('a')
#         if link_tag and link_tag['href']:
#             search_results.append(link_tag['href'])
#             if len(search_results) >= num_results:
#                 break

#     return search_results
