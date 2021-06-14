import json
import requests #make sure to implement this package explicitly if its not present in your IDE

class LoadData:
    'Here we are using Api to get data by passing ID or a query,This cas provides getter functions to get the data'
    def __init__(self):
        self.url='https://forkify-api.herokuapp.com/api/'

    def __makeRequest(self,Url):
        rawdata = requests.get(Url)
        jData = rawdata.text
        data = json.loads(jData)
        return data

    def querySearch(self,query): #It returns a dictionary with two values count and list name recipes of passed query.
        searchUrl=self.url+'search?q='+query
        return self.__makeRequest(searchUrl)

    def idSearch(self,id): #It gives dictionary with one value recipe which is a dictionary with recipe details.
        searchUrl=self.url+'get?rId='+id
        return self.__makeRequest(searchUrl) #Add "['recipe']['publisher']" this at the end of return data to get publisher detail.
