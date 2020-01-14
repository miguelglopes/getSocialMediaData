import Reddit
import News
import Quora
import mySpacy
from MyData import MyDataList

dl = MyDataList()

ss = "Galp"

dl = News.searchandinsert(ss, dl)

dl = Reddit.searchandinsert(ss, dl)

print(dl)

mySpacy.test(dl[61].title)
