import newsapi.newsapi_client as napi
import MyData

#TODO
# meter isto como interface


def searchandinsert(ss, mydatalist):
    news = search(ss)
    return insert(mydatalist, news)


def search(ss, limit=50):

    #TODO
    # implement limit

    client = napi.NewsApiClient(api_key='869f943437634a8f82a582629ac0f62c')

    news = client.get_everything(q=ss, sort_by='relevancy')

    return news


def insert(mydatalist, news):

    for i in news["articles"]:
        do = MyData.MyData()
        do.title = i["title"]
        do.description = i["description"]
        do.fullText = i["content"]
        do.date = i["publishedAt"] #TODO
        do.source = i["source"]["name"]
        do.url = i["url"]
        mydatalist.append(do)

    return mydatalist
