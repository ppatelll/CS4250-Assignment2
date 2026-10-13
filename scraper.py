# AUTHOR: Parth Patel
# FILENAME: scraper.py
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 2 hrs


# Importing Python libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
site = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
front = [seed]
seen = {seed}

# Crawling until the frontier is empty
while front:

    # Removing the first URL from the frontier
    # --> add your Python code here
    url = front.pop(0)

    # Retrieving and parsing the Web page
    # --> add your Python code here
    try:
        ans = requests.get(url,timeout = 10)
        ans.raise_for_status()
    except requests.RequestException as error:
        print(f"Could not retrieve {url}: {error}")
        continue
    temp = BeautifulSoup(ans.text, "html.parser")

    # Printing the text contained in the <h1> element
    # --> add your Python code here
    h = temp.find("h1")
    print(h.get_text(strip=True) if h else "(no <h1> element)")

    # Extracting and processing hyperlinks
    # --> add your Python code here
    webs =[]
    for y in temp.find_all("a", href=True):
        link = urljoin(url, y["href"].strip())
        link, _ = urldefrag(link)
        if link == seed or link.startswith(seed + "/"):
            webs.append(link)
    webs= sorted(set(webs))
    for x in webs:
        if x not in seen:
            seen.add(x)
            front.append(x)

# Printing all URLs in seen
# --> add your Python code here
print("\nThese are the urls in seen:")
for link in sorted(seen):
    print(link)
