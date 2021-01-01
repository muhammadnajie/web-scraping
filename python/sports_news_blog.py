from bs4 import BeautifulSoup
from datetime import date
import datetime
import requests
# import json

TODAY = date.today().strftime("%d-%m-%Y")

def month_id_to_en(date_time):
    bulan = date_time[3:-5]
    dict_of_bulan = {
        "Mei": "May",
        "Agu": "Aug",
        "Okt": "Oct",
        "Des": "Dec"
    }

    converted_month = dict_of_bulan.get(bulan, bulan)
    date_time = date_time.replace(bulan, converted_month)
    return date_time


def detik_sport_news():
    detik_sport_html = requests.get('https://sport.detik.com').text
    detik_soup = BeautifulSoup(detik_sport_html, 'lxml')

    detik_sport_news_articles = detik_soup.find_all('article', {'class': 'gtm_newsfeed_artikel'})
    result = []
    for article in detik_sport_news_articles:
        news_title = article.find('span', {'class': 'labdate'}).next_sibling.strip()
        news_link = article.find('a')['href']
        news_source = article.find('span', {'class': 'label'})
        news_image = article.find('img')['src']

        news_date_time = news_source.next_sibling.strip()
        first_whitespace = news_date_time.index(",")
        news_date = news_date_time[first_whitespace+2:-10].replace(' ', '-')
        news_date = month_id_to_en(news_date)
        news = {
            'title': news_title,
            'image': news_image,
            'date': news_date,
            'source': news_source.text,
            'link': news_link
        }
        result.append(news)
    
    return result


def goal_com_news():
    goal_com_html = requests.get('https://goal.com/id').text
    goal_com_soup = BeautifulSoup(goal_com_html, 'lxml')

    goal_com_news_articles = goal_com_soup.find_all('table', {'class': 'card-type-article'})
    result = []
    for article in goal_com_news_articles:
        news_title_and_link = article.find('h3', {'class': 'widget-news-card__title'})
        news_title = news_title_and_link.text.strip()
        news_link = "https://goal.com/" + news_title_and_link.find('a')['href']
        news_image = article.find('img')['src']
        news = {
            'title': news_title,
            'image': news_image,
            'date': TODAY,
            'source': 'https://goal.com',
            'link': news_link
        }
        result.append(news)

    return result


def pandit_football_news():
    pandit_football_html = requests.get('https://panditfootball.com/').text
    pandit_football_soup = BeautifulSoup(pandit_football_html, 'lxml')

    result = []
    pandit_football_news_articles = pandit_football_soup.find_all('article', {'class': 'news-block'})
    for article in pandit_football_news_articles:
        news_title = article.header.h3.a.text
        news_link = article.header.h3.a['href']
        news_image = article.find('img')['src']
        news_date = article.find('p', {'class': 'simple-share'}).text.replace('/', '-').strip()
        news = {
            'title': news_title.strip(),
            'image': news_image,
            'date': news_date,
            'source': 'Pandit Football Indonesia',
            'link': news_link
        }
        result.append(news)

    return result


source1 = detik_sport_news()
# source2 = goal_com_news()
# source3 = pandit_football_news()

# batch = []
# batch.extend(source1)
# batch.extend(source2)
# batch.extend(source3)

# print()
# print(batch)
# print(source1+source2+source3)

# print(type(source1))