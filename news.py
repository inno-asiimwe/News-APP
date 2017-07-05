import requests

def head_lines(source):
    """A function that prints out the latest headline from a select websites"""
    data = {'source': source, 'apikey':'47c95d8398ab44a4b364a7e9463dc4a3'}
    news = requests.get('https://newsapi.org/v1/articles', params = data)

    if news.status_code == 200:

        news_json = news.json()
        articles = news_json['articles']

        for article in articles:
            print(article['title'])
            print(article['description'])
            print(article['url'])
            print('')
    else:
        print("We are having trouble processing your request, please check your input and try again")


def main():
    """A function that interacts with the users of the news app, it is an entry point for the applicationn"""
    pass



if __name__ == "__main__":
    main()