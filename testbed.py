import requests
from bs4 import BeautifulSoup

# Fetch and parse the page
res = requests.get(
    "https://www.ndr.de/nachrichten/hamburg/bildungssenatorin-bekeris-besucht-lernferiengruppe,bekeris-104.html"
)


def get_text_from_tagesschau(res_):
    soup = BeautifulSoup(res.content, "html.parser")

    # Find the main content container
    content = soup.find("div", class_="layout-content")
    if content:
        for para in content.find_all("p", class_="textabsatz"):
            print(para.text.strip())
    else:
        print("No article content found.")


def get_text_from_ndr(res_):
    soup = BeautifulSoup(res_.content, "html.parser")

    # Find the main content container - use <article> tag instead of div
    content = soup.find("article")
    if content:
        for para in content.find_all("p"):
            print(para.text.strip())
    else:
        print("No article content found.")


get_text_from_ndr(res)
