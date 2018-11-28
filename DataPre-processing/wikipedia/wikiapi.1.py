from bs4 import BeautifulSoup
from hanziconv import HanziConv
import requests


# page = get_web_page(
#     'https://zh.wikipedia.org/wiki/法國歷史年表')
# soup = BeautifulSoup(page, 'html.parser')
# del soup.img["alt"]
# allyear = soup.find('ul').get_text()
# words = allyear.splitlines()

# print(words)
okdict = []


def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


page = get_web_page(
    'https://zh.wikipedia.org/wiki/法國歷史年表')
soup = BeautifulSoup(page, 'html.parser')
del soup.img["alt"]
allyear = HanziConv.toTraditional(soup.find('ul').get_text())
words = allyear.splitlines()

for i in words:
    i = i.split('：')
    try:
        i[0] = int(i[0][:-1])
    except:
        i[0] = i[0].split('-')
        try:
            i[0][0] = int(i[0][0][:-1])
            i[0][1] = int(i[0][1][:-1])
        except:
            pass
        if len(i[0]) > 1:
            event = {
                "title": i[1],
                "category": "political",
                "yearFrom": str(i[0][0]),
                "yearTo": str(i[0][1]),
                "city": "法國"
            }
            # eventsTable.insert_one(event)
    # print(i)

# 法國
