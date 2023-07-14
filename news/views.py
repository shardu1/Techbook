from django.shortcuts import render,HttpResponse
from newsapi import NewsApiClient
from news.models import News

# Create your views here.
def newsHome(request):
    allNews= News.objects.all()
    context={'allNews':allNews}
    return render(request,'news/index.html',context)
    # return render(request,'news/n-index.html')

def newsPost(request,slug):
    post = News.objects.filter(slug=slug)[0]
    context = {'post':post}
    return render(request,'news/post-page.html',context)

def technology(request):
    newsapi = NewsApiClient(api_key='4172d085084342e58d094296122b13af')
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

        newsblog = News(
            author=author,
            title=title,
            imgurl=imgurl,
            newsurl=newsurl,
            description=description,
            query='blockchain',
            date=date,
            slug=title.replace(" ",'-')
            )
        newsblog.save()
    print("Tecnology news done.")
    return HttpResponse(request,"Technology done")