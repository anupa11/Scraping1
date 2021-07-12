from bs4 import BeautifulSoup
import requests
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')

# print(article.prettify())
vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
# print(vid_id)
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)