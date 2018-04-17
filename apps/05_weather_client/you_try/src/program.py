#!/usr/bin/env python3
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    print_header()
    zip_code = int(input('Enter zip code: '))
    html = download_html(zip_code)
    report = parse_weather(html)
    print('The temp in {} is {} and {}{}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale
    ))
    pass


def print_header():
    print('---------------------------------------------------------------')
    print('                         WEATHER APP')
    print('---------------------------------------------------------------')
    print()


def download_html(zip_code: int):
    url = 'https://www.wunderground.com/weather/us/dc/washington/{}'.format(zip_code)
    response = requests.get(url)
    return response.text


def parse_weather(html: str):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_="region-content-header").find('h1').get_text().strip()
    condition = soup.find(class_="condition-icon").get_text().strip()
    temp = soup.find(class_="wu-unit-temperature").find(class_="wu-value").get_text().strip()
    scale = soup.find(class_="wu-unit-temperature").find(class_="wu-label").get_text().strip()
    return WeatherReport(loc=loc, cond=condition, temp=temp, scale=scale)


if __name__ == '__main__':
    main()
