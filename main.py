# pip install beautifulsoup4-#разбиват HTML файлы
# pip install requests-позволяет создавать http-запросы
# pip install pandas-библиотека анализа данных
import requests
from bs4 import BeautifulSoup
import pandas
import glob
from collections import OrderedDict

from requests import Request
from urllib3 import request

# pages_csv = 'characters_pages.csv'
# characters_csv = 'characters_dataset.csv'
#
#
# # получение ссылок и их обработка
# def get_all_links():
#     # запрс данных с сайта
#     page = requests.get('https://www.marvel.com/characters')
# # вызов конвертера данных HTML-структуры сайта
#     soup = BeautifulSoup(page.content, 'html.parser')
#
#     pages = []
# # Поиск данных из файла по структуре HTML
#     mvl_cards = (soup.find('div', {'class': 'full-content'}).
#                  find_all('div', {'class': 'mvl-card mvl-card-explore'}))
#     for i in range(len(mvl_cards) - 1):
#         link = mvl_cards[i]
#         page = link.find('a')
#         print(i, page['href'], page.text)
#         pages.append(page['href'])
#     df = pandas.DataFrame({'Link': pages})
#     write_csv_file(df, pages_csv)
#
#
# # запись файла в csv-формат
# def write_csv_file(df, name):
#     df.to_csv(name, index=False)
#     print('успешно выполнено ! \n')
#
#
# def read_csv_file(name):
#     df = pandas.read_csv(name)
#     return df
#
#
# # обратимся к полученному файлу, чтение
# def create_characters_df():
#     base_url = 'https://www.marvel.com'
#     pages = pandas.read_csv(pages_csv)
#     links = pages['Link']
#     columns = []
#     marvel_list = []
#     # проход по всем ссылкам записанным в csv
#     for link in links:
#         marvel_characters = OrderedDict()
#         # получение данных из карточки каждого персонажа с сайта
#         request = requests.get(base_url + str(link))
#
#         content = request.content
#         soup = BeautifulSoup(content, 'html.parser')
#
#         marvel_characters['Name'] = soup.find('h1').text.replace('\n', '').strip()
#         marvel_characters['Link'] = link
#         print(soup.find('h1').text.replace('\n', '').text.replace('\n', ''), base_url + str(link))
#         # поиск описания персонажа
#         label = soup.findAll('p', {'class': 'bioheader__label'})
#         stat = soup.findAll('p', {'class': 'bioheader__stat'})
#         for i in range(len(label)):
#             column = label[i].text.title()
#             if column not in columns:
#                 column.appened(column)
#             try:
#                 marvel_characters[column] = stat[i].text.replace('\n', '').strip()
#             except:
#                 marvel_characters[column] = ''
#         marvel_list.append(marvel_characters)
#     df = pandas.DataFrame(marvel_list)
#     write_csv_file(df, characters_csv)
#
# def main():
#     files = glob.glob('*, .csv')
#     if characters_csv not in files:
#         if pages_csv not in files:
#             print('создание файла characters_pages.csv')
#             get_all_links()
#         print('создание файла characters_pages.csv')
#         create_characters_df()
#     df=read_csv_file(characters_csv)
#     df=df.fillna('')
#     print('колонки:', df.colums.values)
#     print(df[['link','Eyes']])
# # чтение данных из файла и отображение
#     df =pandas.read_csv('characters_dataset.csv')
# # размеры файла
#     print(df.shape)

from bs4 import BeautifulSoup
import requests
import pandas
import glob
from collections import OrderedDict

pages_csv = 'characters_pages.csv'
characters_csv = 'characters_dataset.csv'


def get_all_links():
    page = requests.get('https://www.marvel.com/characters')
    soup = BeautifulSoup(page.content, 'html.parser')

    pages = []
    mvl_cards = (soup.find('div', {'class': 'grid-base grid__6'}).
                find_all('div', {'class': 'mvl-card mvl-card--explore'}))
    for i in range(len(mvl_cards)-1):
        link = mvl_cards[i]
        page = link.find('a', {'class': 'explore__link'} )
        print(i, page['href'], page.text)
        pages.append(page['href'])

    df = pandas.DataFrame({'Link': pages})
    write_csv_file(df, pages_csv)


def create_characters_df():
    base_url = 'https://www.marvel.com'
    pages = pandas.read_csv(pages_csv)
    links = pages['Link']
    marvel_list = []
    columns = []

    for link in links:
        marvel_characters = OrderedDict()
        request = requests.get(base_url + str(link))

        content = request.content
        soup = BeautifulSoup(content, 'html.parser')

        marvel_characters['Name'] = soup.find("h1").text.replace("\n", "").strip()
        marvel_characters['Link'] = link
        print(soup.find('h1').text.replace("\n", "").strip(), base_url + str(link))

        label = soup.findAll('p', {'class': 'bioheader__label'})
        stat = soup.findAll('p', {'class': 'bioheader__stat'})

        for i in range(len(label)):
            column = label[i].text.title()
            if column not in columns:
                columns.append(column)
            try:
                marvel_characters[column] = stat[i].text.replace('\n', '').strip()
            except:
                marvel_characters[column] = ''

        marvel_list.append(marvel_characters)
    df = pandas.DataFrame(marvel_list)
    write_csv_file(df, characters_csv)


def write_csv_file(df, name):
    df.to_csv(name, index=False)
    print('Success \n')


def read_csv_file(name):
    df = pandas.read_csv(name)
    return df


def main():
    files = glob.glob('*.csv')

    if characters_csv not in files:
        if pages_csv not in files:
            print('Create characters_pages.csv')
            get_all_links()
        print('Create characters_dataset.csv')
        create_characters_df()

    df = read_csv_file(characters_csv)
    df = df.fillna('')
    print('Columns: ', df.columns.values)
    print(df[['Link', 'Eyes']])
    df = pandas.read_csv('characters_dataset.csv')
    print(df.shape)  # размеры файла

if __name__ == '__main__':
    main()





