from urllib import request
import random
import bs4


def craw_search(input):
    url = 'https://nhentai.net/search/?q='
    input = input.replace('[', '%5B')
    input = input.replace(']', '%5D')
    input = input.replace('(', '%28')
    input = input.replace(')', '%29')
    input = input.replace('|', '%7C')
    input = input.replace('\'', '%27')
    input = input.replace('+', '%2B')
    input = input.replace(' ', '+')
    input = input.replace('!', '%21')
    url += input
    r = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                                      'cookie': 'csrftoken=kz6gpJ5P33Q955XlsTY0SOviS2Lgj5pjVdf92RzV5Yxx5UuTyPb3I5VhepwbYPwS; cf_clearance=.nQAHsuw4Znszo.gNjq20YgNMupssanO2q4tt7SYay4-1672000464-0-150'})
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    second = []
    third = []
    for i in range(5):
        second.append('https://nhentai.net')
    count = 0
    titles = root.find_all('div', class_='gallery')
    for i in titles:
        second[count] += i.a['href']
        count += 1
        if (count == 5):
            break
    count = 0
    for i in titles:
        k = i.a.find('img', class_='lazyload')
        third.append(k['data-src'])
        count += 1
        if (count == 5):
            break
    return second, third


def craw_random():
    url = 'https://nhentai.net/g/'
    url += str(random.randint(1, 433376))
    r = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                                      'cookie': 'csrftoken=kz6gpJ5P33Q955XlsTY0SOviS2Lgj5pjVdf92RzV5Yxx5UuTyPb3I5VhepwbYPwS; cf_clearance=.nQAHsuw4Znszo.gNjq20YgNMupssanO2q4tt7SYay4-1672000464-0-150'})
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    titles = root.find('div', class_='gallery')
    second = titles.a.find('img', class_='lazyload')
    third = root.find('h2', class_='title').find('span', class_='pretty')
    # print(url)
    # print(second['data-src'])
    # print(third.text)
    return url, second['data-src'], third.text


def craw_tags(input):
    url = 'https://nhentai.net/tag/'
    input = input.replace('[', '%5B')
    input = input.replace(']', '%5D')
    input = input.replace('(', '%28')
    input = input.replace(')', '%29')
    input = input.replace('|', '%7C')
    input = input.replace('\'', '%27')
    input = input.replace('+', '%2B')
    input = input.replace(' ', '+')
    input = input.replace('!', '%21')
    url += input
    r = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                                      'cookie': 'csrftoken=kz6gpJ5P33Q955XlsTY0SOviS2Lgj5pjVdf92RzV5Yxx5UuTyPb3I5VhepwbYPwS; cf_clearance=.nQAHsuw4Znszo.gNjq20YgNMupssanO2q4tt7SYay4-1672000464-0-150'})
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    second = []
    third = []
    for i in range(5):
        second.append('https://nhentai.net')
    count = 0
    titles = root.find_all('div', class_='gallery')
    for i in titles:
        second[count] += i.a['href']
        count += 1
        if (count == 5):
            break
    count = 0
    for i in titles:
        k = i.a.find('img', class_='lazyload')
        third.append(k['data-src'])
        count += 1
        if (count == 5):
            break
    return second, third

def craw_language(input):
    url = 'https://nhentai.net/language/'
    url += input
    r = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                                      'cookie': 'csrftoken=kz6gpJ5P33Q955XlsTY0SOviS2Lgj5pjVdf92RzV5Yxx5UuTyPb3I5VhepwbYPwS; cf_clearance=.nQAHsuw4Znszo.gNjq20YgNMupssanO2q4tt7SYay4-1672000464-0-150'})
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    second = []
    third = []
    for i in range(5):
        second.append('https://nhentai.net')
    count = 0
    titles = root.find_all('div', class_='gallery')
    for i in titles:
        second[count] += i.a['href']
        count += 1
        if (count == 5):
            break
    count = 0
    for i in titles:
        k = i.a.find('img', class_='lazyload')
        third.append(k['data-src'])
        count += 1
        if (count == 5):
            break
    return second, third