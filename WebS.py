import requests
from bs4 import BeautifulSoup
KEYWORDS = ['дизайн', 'фото', 'web', 'python']





def get_articles():
    response = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(response.text,'html.parser')
    all_articles = soup.find_all('article', class_= 'tm-articles-list__item')
    return all_articles





def search(words):
    articles = []
    for article in get_articles():
        for word in words:
            items = []   
            if word in article.text:
                name = article.find("a", class_= 'tm-article-snippet__title-link').text
                link = article.find("a", class_= 'tm-article-snippet__title-link')['href']
                date = article.find("span", class_= 'tm-article-snippet__datetime-published').text
                items.append(name)
                items.append(date)
                items.append(link)
                articles.append(items)
    for artic in articles:
        print(f'<{artic[0]}> - <{artic[1]}> - <{artic[2]}>')





search(KEYWORDS)


# In[ ]:





# In[ ]:




