
import requests

response = requests.get("https://newsapi.org/v2/everything?q=defence&from_param='2023-07-09'&to=2023-07-15&language=en&sort_by=relevancy&apiKey=57f5447c13ba4f98abb41bfe6350d7fb")

json_body = response.json()
articles=json_body['articles']


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