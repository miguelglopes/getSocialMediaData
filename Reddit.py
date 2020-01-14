import praw
import MyData

#TODO
# meter isto como interface


def searchandinsert(ss, mydatalist):
    news = search(ss)
    return insert(mydatalist, news)


def search(ss, limit=50):
    clientid = "4AdTkc8qDnhMDg"
    clientsecret = "hdG9-oGY_ybBoZO54j2UpuLui58"
    password = "`yaH6?9HxG*2nG8:"
    useragent = "migasll script"
    username = "migasll8"

    reddit = praw.Reddit(client_id=clientid,
                         client_secret=clientsecret,
                         password=password,
                         user_agent=useragent,
                         username=username)

    allresults = reddit.subreddit("all")

    return allresults.search(ss, limit=limit)


def insert(mydatalist, news):

    for i in news:
        do = MyData.MyData()
        do.title = i.title
        do.description = "TODO" #TODO
        do.fullText = "TODO" #TODO
        do.date = i.created #TODO
        do.source = i.subreddit_name_prefixed
        do.url = i.url
        mydatalist.append(do)

    return mydatalist
