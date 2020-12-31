from bs4 import BeautifulSoup
from datetime import date
import requests
# import json

TODAY = date.today().strftime("%d-%m-%Y")

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
        news_date = news_source.next_sibling.strip()[2:-4]
        news = {
            'title': news_title,
            'image': news_image,
            'date': news_date,
            'source': news_source.text,
            'link': news_link
        }
        result.append(news)
    
    # print(result)

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

    # print(result)

# detik_sport_news()
# goal_com_news()
