from newsapi import NewsApiClient

API_KEY = 'Add your own API key here'
newsApi = NewsApiClient(api_key = API_KEY)

def get_user_choice():
       country = input("Enter the country to get the relevant news from(2-letter ISO code): ")
       category = input("Enter the category for news (business, entertainment, general, health, science, sports, technology): ")
       keyword = input("What topic are you looking for: ")
       return country, category, keyword

def get_top_headlines():
       country, category, keyword = get_user_choice()
       top_headlines = newsApi.get_top_headlines(q=keyword,
                                          country=country,
                                          category=category,
                                          language='en')
       organize_response(top_headlines)

def get_all_articles():
       all_articles = newsApi.get_everything(q='cryptocurrency',
                                      sources='bbc-news',
                                      domains='bbc.co.uk',
                                      from_param='2021-12-10',
                                      to='2022-01-01',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
       organize_response(all_articles)

def organize_response(top_headlines):
       for headline in top_headlines['articles']:
              source = headline['source']['name']
              author = headline['author']
              title = headline['title']
              url = headline['url']
              print("Source: {}\nAuthor: {}\nTitle: {}\nURL: {}".format(source, author, title, url))
              print('==================================================================')


# Call the appropriate function
# get_top_headlines()
# get_all_articles()