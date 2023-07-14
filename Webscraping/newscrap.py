from newsapi import NewsApiClient
# from news.models import News
# Init
newsapi = NewsApiClient(api_key='4172d085084342e58d094296122b13af')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/everything
technology = newsapi.get_everything(
        q='India+Technology',
        from_param='2023-07-07',
        to='2023-07-14',
        language='en',

        
    )

articles = technology['articles']

for article in articles:
    author=article['author']
    title=article['title']
    imgurl=article['urlToImage']
    newsurl=article['url']
    description=article['description']
    date=article['publishedAt'][:10]

    # news = News(
    #     author=author,
    #     title=title,
    #     imgurl=imgurl,
    #     newsurl=newsurl,
    #     description=description,
    #     query='technology',
    #     date=date
    #     )
    # news.save()
    print(title)    
# print("Tecnology news done.")
    

print(len(technology['articles']))
# print(technology['articles'][1]['title'])
# print(technology['articles'][1]['publishedAt'][:10])

# /v2/top-headlines/sources
# sources = newsapi.get_sources()