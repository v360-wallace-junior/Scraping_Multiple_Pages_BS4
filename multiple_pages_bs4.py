import requests
from bs4 import BeautifulSoup
from pathlib import Path
import cloudscraper

root = 'https://subslikescript.com/'
website = f'{root}/movies'

# captcha_url = 'https://subslikescript.com/challenge?destination=%2Fmovies'

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True
    }
)

try:

    response = scraper.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())


    print(response.url)

    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    print(title)
    # print(box)

    links = []
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    print(links)

    # Criar pasta e Arquivos
    fold = Path('./textos')
    fold.mkdir(parents=True, exist_ok=True)

    for link in links:
        website = f'{root}/{link}'
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('article', class_='main-article')

        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')


        with open(f'./textos/{title}.txt', 'w') as file:
            file.write(transcript)


except Exception as e:
    print(f"Erro ao tentar acessar a página: {e}")

