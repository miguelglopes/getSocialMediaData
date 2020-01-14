class MyData:

    title = None
    description = None
    fullText = None
    date = None
    source = None
    url = None

    def __str__(self):
        return "%s - %s" % (self.date, self.title)


class MyDataList(list):

    dummy = None

    def __init__(self):
        self.dummy = None

    def __str__(self):
        for i in self:
            print(i)
        return ""


