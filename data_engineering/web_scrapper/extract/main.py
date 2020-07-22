""" Initial configuration"""

#python3
import argparse
import logging
import re
import datetime
import csv

#errors
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

#data_engineering
from common import config
import news_page_objects as news

#logging basic configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#regular expresions
is_well_formed_url= re.compile(r'^https?://.+/.+$') # i.e. https://www.somesite.com/something
is_root_path = re.compile(r'^/.+$') # i.e. /some-text
 

def _news_scraper(news_site_uid):
    """scraping´s initialitation and main funcion to conect, fetching and save 
    all news in the web-papers """
    host = config()['news_sites'][news_site_uid]['url']
    homepage= news.HomePage(news_site_uid, host) # paper , url
    logging.info(f'Beginning scraper for {host}')
    logging.info('Finding links in homepage...')
    articles=[]
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)
        if article:
            logger.info('Article fetched !!')
            articles.append(article)
        #break #onli dev
    _save_articles(news_site_uid, articles)
    


def _save_articles(news_site_uid, articles):
    now= datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f'{news_site_uid}_{now}_articles.csv'
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))
    with open(out_file_name, mode='w+',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)

           

def _fetch_article(news_site_uid, host, link):
    logger.info(f'Start fetching article at {link}')
    article =None
    try:
        article = news.ArticlePage(news_site_uid, _build_links(host, link))
    except (HTTPError,MaxRetryError) as e:
        logger.warning('Error while fechting the article', exc_info = False)
    if article and not article.body:
        logger.warning('Invaid article. There is no body')
        return None
    return article   

def _build_links(host, link):
    if is_well_formed_url.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return f'{host}/{link}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    news_site_choices = list(config()['news_sites'].keys()) #papers
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)

    args = parser.parse_args()
    _news_scraper(args.news_site) #paper