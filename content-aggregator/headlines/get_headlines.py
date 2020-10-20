import requests
from bs4 import BeautifulSoup

from headlines import MinorHeadline, MainHeadline, Website


def get_main_headline(soup_object, site_url):
    main_headline = soup_object.find_all('h1')
    text = main_headline[0].a.text
    url = main_headline[0].a['href']
    if url.startswith('/'):
        url = site_url + url
    return MainHeadline(text, url)


def get_minor_headlines(soup_object):
    text_headlines = soup_object.find_all('h2')
    return list(map(lambda headline: MinorHeadline(headline.text), text_headlines))


def get_all_headlines(url):
    r = requests.get(url)
    r_html = r.content
    soup = BeautifulSoup(r_html, "html.parser")
    website_name = url.split('/')[-1].split('.')[0]
    main_headline = get_main_headline(soup, url)
    minor_headlines = get_minor_headlines(soup)
    return Website(main_headline, minor_headlines, website_name)
