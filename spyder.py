__author__ = 'Administrator'
import requests  # http lib
from bs4 import BeautifulSoup  # climb lib
import os # operation system
import traceback # trace deviance



class konachan_spyder():
    def __init__(self, tag):
        self.tag = tag

    def __download(self, url, filename):
        if os.path.exists(filename):
            print('file exists!')
            return
        try:
            r = requests.get(url, stream=True, timeout=60)
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alove new chunks
                        f.write(chunk)
                        f.flush()
            return filename
        except KeyboardInterrupt:
            if os.path.exists(filename):
                os.remove(filename)
            return KeyboardInterrupt
        except Exception:
            traceback.print_exc()
            if os.path.exists(filename):
                os.remove(filename)

    def konachan_spyder(self):
        if os.path.exists('imgs') is False:
            os.makedirs('imgs')
        start = 1
        #tag = 'card_captor_sakura'
        url = 'http://konachan.net/post?page=1&tags=' + self.tag
        html = requests.get(url).text
        from lxml import etree
        selector = etree.HTML(html)
        end = int(selector.xpath('//*[@class="next_page"]/preceding-sibling::a[1]/text()')[0])
        for i in range(start, end+1):
            url = 'http://konachan.net/post?page='+str(i)+'&tags='+self.tag
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            for span in soup.find_all('span', class_="plid"):# 遍历所有preview类，找到img标签
                target_url = span.text.split(' ')[1]
                html = requests.get(target_url).text
                soup = BeautifulSoup(html, 'html.parser')
                for img in soup.find_all('img', class_="image"):
                    target_url = img['src']
                filename = os.path.join('imgs', target_url.split('/')[-1])
                self.__download(target_url, filename)
            print('%d / %d' % (i, end))


if __name__ =='__main__':
    sp = konachan_spyder('card_captor_sakura')
    sp.konachan_spyder()