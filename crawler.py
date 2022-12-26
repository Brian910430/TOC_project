from urllib import request
import random
import bs4

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
          'cookie': 'csrftoken=kz6gpJ5P33Q955XlsTY0SOviS2Lgj5pjVdf92RzV5Yxx5UuTyPb3I5VhepwbYPwS; cf_chl_2=8b24b16ad0d34d1; cf_clearance=uCtsxc5CTopt8lccRXgWQYXkXbN0Ou.4TaHpAIkjyN4-1672057317-0-150'}


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
    r = request.Request(url, headers=header)
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    urls = []
    imgs = []
    tls = []
    titles = root.find_all('div', class_='gallery')
    for i in range(5):
        choose = titles[random.randint(0, len(titles) - 1)]
        urls.append('https://nhentai.net')
        urls[i] += choose.a['href']
        k = choose.a.find('img', class_='lazyload')
        imgs.append(k['data-src'])
        titles.pop(titles.index(choose))

    for i in range(5):
        tempUrl = urls[i]
        tempReq = request.Request(tempUrl, headers=header)
        with request.urlopen(tempReq) as response:
            tempData = response.read().decode('utf-8')
        tempRoot = bs4.BeautifulSoup(tempData, 'html.parser')
        temp = tempRoot.find('h2', class_='title').find(
            'span', class_='pretty')
        tls.append(temp.text)
        if (len(tls[i]) > 20):
            tls[i] = tls[i][0:20] + '...'
    return urls, imgs, tls


def craw_random():
    url = 'https://nhentai.net/g/'
    url += str(random.randint(1, 433376))
    r = request.Request(url, headers=header)
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    titles = root.find('div', class_='gallery')
    second = titles.a.find('img', class_='lazyload')
    third = root.find('h2', class_='title').find('span', class_='pretty')
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
    input = input.replace(' ', '-')
    input = input.replace('!', '%21')
    url += input
    r = request.Request(url, headers=header)
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    urls = []
    imgs = []
    tls = []
    titles = root.find_all('div', class_='gallery')
    for i in range(5):
        choose = titles[random.randint(0, len(titles) - 1)]
        urls.append('https://nhentai.net')
        urls[i] += choose.a['href']
        k = choose.a.find('img', class_='lazyload')
        imgs.append(k['data-src'])
        titles.pop(titles.index(choose))

    for i in range(5):
        tempUrl = urls[i]
        tempReq = request.Request(tempUrl, headers=header)
        with request.urlopen(tempReq) as response:
            tempData = response.read().decode('utf-8')
        tempRoot = bs4.BeautifulSoup(tempData, 'html.parser')
        temp = tempRoot.find('h2', class_='title').find(
            'span', class_='pretty')
        tls.append(temp.text)
        if (len(tls[i]) > 20):
            tls[i] = tls[i][0:20] + '...'

    return urls, imgs, tls


def craw_language(input):
    url = 'https://nhentai.net/language/'
    url += input
    r = request.Request(url, headers=header)
    with request.urlopen(r) as response:
        data = response.read().decode('utf-8')
    root = bs4.BeautifulSoup(data, 'html.parser')
    urls = []
    imgs = []
    tls = []
    titles = root.find_all('div', class_='gallery')
    for i in range(5):
        choose = titles[random.randint(0, len(titles) - 1)]
        urls.append('https://nhentai.net')
        urls[i] += choose.a['href']
        k = choose.a.find('img', class_='lazyload')
        imgs.append(k['data-src'])
        titles.pop(titles.index(choose))

    for i in range(5):
        tempUrl = urls[i]
        tempReq = request.Request(tempUrl, headers=header)
        with request.urlopen(tempReq) as response:
            tempData = response.read().decode('utf-8')
        tempRoot = bs4.BeautifulSoup(tempData, 'html.parser')
        temp = tempRoot.find('h2', class_='title').find(
            'span', class_='pretty')
        tls.append(temp.text)
        if (len(tls[i]) > 20):
            tls[i] = tls[i][0:20] + '...'
    return urls, imgs, tls
