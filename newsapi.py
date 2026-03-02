import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

tagesschau = {
    "hamburg": "https://www.tagesschau.de/api2u/news/?regions=6",
    "nrw": "https://www.tagesschau.de/api2u/news/?regions=10",
    "inland": "https://www.tagesschau.de/api2u/news/?ressort=inland",
    "ausland": "https://www.tagesschau.de/api2u/news/?ressort=ausland",
    "wissen": "https://www.tagesschau.de/api2u/news/?ressort=wissen",
}


def get_text_from_tagesschau(res_):
    soup = BeautifulSoup(res_.content, "html.parser")

    # Find the main content container
    content = soup.find("div", class_="layout-content")
    if content:
        for para in content.find_all("p", class_="textabsatz"):
            print(para.text.strip())
    else:
        print("No article content found.")


def get_response(hyperlink):
    response = requests.get(hyperlink)
    if response.status_code != 200:
        return
    return response


def get_headlines(response):
    counter = 0
    rdict = response.json()
    resultdict = {}
    for key, value in rdict.items():
        if key == "news":
            for element in value:
                articledate = datetime.strptime(element.get("date")[:10], "%Y-%m-%d")
                if datetime.now() - articledate > timedelta(days=3):
                    continue
                outputdate = datetime.strftime(articledate, "%d.%m.%Y")
                tdelta = datetime.now() - articledate
                counter += 1
                resultdict[counter] = {
                    "ago": tdelta.days,
                    "date": outputdate,
                    "breaking_news": element.get("breakingNews"),
                    "title": element.get("title"),
                    "subtitle": element.get("firstSentence"),
                    "link": element.get("detailsweb")
                    }

def get_all_news():
    all_news = {}
    for ressort, apilink in tagesschau.items():
        all_news[ressort]=get_headlines(get_response(apilink))
    print("Tagesschau API: https://tagesschau.api.bund.dev/")


get_all_news()
