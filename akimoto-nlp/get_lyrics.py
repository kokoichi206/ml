import requests
import os
from bs4 import BeautifulSoup
from typing import List, Tuple


"""
Base となる歌詞検索サイト
https://www.uta-net.com/search/
"""
class FetchLyrics():
    def __init__(self):
        # Webページを取得して解析する
        self.BASE_URL = "https://www.uta-net.com"

    def get_search_url(self, group, page=1):
        return f"https://www.uta-net.com/search/?Aselect=1&Bselect=3&Keyword={group}&sort=&pnum={page}"

    def get_dom(self, url):

        # BeautifulSoupオブジェクト生成
        headers = {'User-Agent': 'Mozilla/5.0'}

        # URLの情報を取得
        return BeautifulSoup(
            requests.get(url, headers=headers).content,'html.parser')   

    def get_max_pages(self, group):

        url = self.get_search_url(group)
        soup = self.get_dom(url)

        # FIXME
        # 何回も取得したくないけど、どこで保存とかどこで何をやらせるべきかわからん
        self.soup = soup

        # 全ページ数表示 div タグ
        pages = soup.findAll('div', class_='upper_page_list')
        
        if not len(pages) == 1:
            print("ERROR: 全ページ数表示 div タグ取得失敗")
            return
        
        span_elms = pages[0].findAll('span', class_='pa')
        if not len(span_elms) == 1:
            print("ERROR: 全ページ数表示 span タグ取得失敗")
            return
        
        # expected:「全2ページ中　1ページを表示」
        text = span_elms[0].text
        page_num = text.split('ページ')[0][1:]

        return int(page_num)
    
    def get_all_lyrics_for_one_page(self, group: str, page: int) -> Tuple[List[str], List[str]]:
        titles = []
        lyrics = []

        url = self.get_search_url(group=group, page=page)
        soup = self.get_dom(url)

        # 複数箇所に分かれて tbody が存在する
        tbodys = soup.findAll('tbody')
        for tbody in tbodys:
            trs = tbody.findAll('tr')

            # 行でループ
            for tr in trs:
                tds = tr.findAll('td')

                is_akimoto = False
                # 列で見ていく
                for td in tds:
                    if td.text == '秋元康':
                        is_akimoto = True

                if is_akimoto:
                    a_tag = tds[0].findAll('a')[0]
                    path = a_tag.attrs['href']
                    ly = self.get_one_song_lyrics(path).replace('\u3000', ' ')

                    titles.append(a_tag.text)
                    lyrics.append(ly)
        
        return titles, lyrics

    # relative_path: /hoge/pien
    def get_one_song_lyrics(self, relative_path: str) -> str:
        url = self.BASE_URL + relative_path
        soup = self.get_dom(url)

        # TODO: 訓練する際に、以下を考える
        # 改行とか消えてしまうけどいいかな？
        return soup.find('div', id='kashi_area').text

    def save_lyrics(self, group: str, titles: List[str], lyrics: List[str]):
        save_dir = './lyrics'
        os.makedirs(save_dir, exist_ok=True)

        with open(f'{save_dir}/{group}_titles.txt', mode='a') as f:
            titles = '\n'.join(titles)
            f.write(f'{titles}')
        with open(f'{save_dir}/{group}_lyrics.txt', mode='a') as f:
            lyrics = '\n'.join(lyrics)
            f.write(f'{lyrics}')

    def main(self):
        groups = ['乃木坂', '櫻坂', '日向坂']
        for group in groups:
            page_num = self.get_max_pages(group)
            # 保存した歌詞数
            cnt = 0
            for i in range(1, page_num+1):
                titles, lyrics = self.get_all_lyrics_for_one_page(group, i)
                cnt += len(titles)
                self.save_lyrics(group=group, titles=titles, lyrics=lyrics)
            print(f"%s:%4d曲分の歌詞を保存しました" % (group, cnt))


if __name__ == "__main__":
    fetcher = FetchLyrics()
    fetcher.main()
