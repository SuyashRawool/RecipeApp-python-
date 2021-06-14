from LoadApi import LoadData
from autocorrect import Speller #pip install autocorrect ,link:https://github.com/fsondej/autocorrect
import asyncio


class SearchEngine:
    'This is searchEngine class'

    def __init__(self):
        self.ld=LoadData()


    def checkWord(self,word):#use it in main class , returns None if all good
        if(len(word.split())>1):
            return 'Please Use One word'

    def availabeQueries(self):
        return 'https://forkify-api.herokuapp.com/phrases.html'

    def searchQuery(self,word): #Aproach LoadApi through this function only
        data=self.ld.querySearch(word)

        if(list(data.keys())[0]=='error'): #this condition only occurs if Api returns an error
            spell = Speller()
            data=ld.querySearch(spell(word))
            return data

        return data

    def getRecipe(self,id):
        data=self.ld.idSearch(id)['recipe']['ingredients']
        str=""
        for i in data:
            str+="-> "+i+".\n"
        return str

    def getPublisher(self,id):
        return self.ld.idSearch(id)['recipe']['publisher']

    def getTitle(self,id):
        return self.ld.idSearch(id)['recipe']['title']

    def getSourceUrl(self,id):
        return self.ld.idSearch(id)['recipe']['source_url']

    def getImage(self,id):
        return self.ld.idSearch(id)['recipe']['image_url']

    def getPublisherUrl(self,id):
        return self.ld.idSearch(id)['recipe']['publisher_url']

    def getRank(self,id):
        return self.ld.idSearch(id)['recipe']['social_rank']

