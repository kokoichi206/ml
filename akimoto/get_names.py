import requests
from bs4 import BeautifulSoup

def get_dom(url: str):

    # BeautifulSoupオブジェクト生成
    headers = {'User-Agent': 'Mozilla/5.0'}

    # URLの情報を取得
    return BeautifulSoup(
        requests.get(url, headers=headers).content,'html.parser')


def nogi_names():

    TOP_URL = 'https://www.nogizaka46.com/member'
    soup = get_dom(TOP_URL)
    details = soup.findAll('div', class_='unit')

    names = []
    for detail in details:
        span = detail.find("span", class_='main')
        name = span.text
        if name not in names:
            names.append(name)

    return names

def sakura_names():
    TOP_URL = 'https://sakurazaka46.com/s/s46/search/artist'

    soup = get_dom(TOP_URL)
    details = soup.findAll('li', class_='box')

    names = []
    for detail in details:
        # li の中には、thumb(div>img), name, kana の順番で div が格納されている
        div_tags = detail.findAll('p')
        name = div_tags[0].text.strip()
        if name not in names:
            names.append(name)

    return names

def hinata_names():

    # URL 構成の感じ、めっちゃ桜坂と似てる！！
    TOP_URL = 'https://www.hinatazaka46.com/s/official/search/artist'

    soup = get_dom(TOP_URL)
    details = soup.findAll('li', class_='p-member__item')

    names = []
    for detail in details:
        # li の中には、thumb(div>img), name, kana の順番で div が格納されている
        div_tags = detail.findAll('div')
        name = div_tags[1].text.strip()
        if name not in names:
            names.append(name)
    
    return names

def akb_names():
    TOP_URL = 'https://www.akb48.co.jp/about/members'

    soup = get_dom(TOP_URL)
    details = soup.findAll('div', class_='memberProf')

    names = []
    for detail in details:
        p_tags = detail.findAll('p')
        name = p_tags[0].text
        if name not in names:
            names.append(name)
    
    return names

def saka():
    saka = []
    saka += nogi_names()
    saka += sakura_names()
    saka += hinata_names()
    print(saka)
    return saka

def akb():
    akb = []
    akb += akb_names()
    print(akb)
    return akb

if __name__ == '__main__':
    # saka = nogi_names()
    # # saka.append(sakura_names())
    # saka += sakura_names()
    # # saka.append(hinata_names())
    # saka += hinata_names()
    # print(saka)
    print(len(akb()))
    # print(len(saka()))
