from LoadApi import LoadData
#from autocorrect import Speller #pip install autocorrect ,link:https://github.com/fsondej/autocorrect



class SearchEngine:
    'This is searchEngine class'
    def __init__(self):
        self.ld=LoadData()


    def checkWord(self,word):#use it in main class , returns None if all good
        if(len(word.split())>1):
            return False
        return True

    def availabeQueries(self):
        return 'https://forkify-api.herokuapp.com/phrases.html'

    def searchQuery(self,word): #Aproach LoadApi through this function only
        data=self.ld.querySearch(word)



        return data

    def setData(self,id):
        self.data = self.ld.idSearch(id)

    #the functions with 'f' are fast functions these take load time once
    def getRecipef(self):
        return self.data['recipe']['ingredients']


    def getPublisherf(self):
        return self.data['recipe']['publisher']

    def getTitlef(self):
        return self.data['recipe']['title']

    def getSourceUrlf(self):
        return self.data['recipe']['source_url']

    def getImagef(self):
        return self.data['recipe']['image_url']

    def getPublisherUrlf(self):
        return self.data['recipe']['publisher_url']

    def getRankf(self):
        return self.data['recipe']['social_rank']

    #these are seperate search functions these will take time to load data
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

