import json
class LoadJson:
    'This class loads a JSON file and returns components of the file using getter functions'

    def __init__(self):#way,0 from json & 1 for database
        self.f=open('src/recipe.json')
        self.data=json.load(self.f)


    def getRecipe(self,title):#This function returns a list so use a for loop to display the steps
        for d in self.data:
            if title in d['name']:
                return d['steps']
        return 'Not Found!'

    def getIngrediants(self,title):#It returns a list of dictionary
        for d in self.data:
            if title in d['name']:
                return d['ingredients']
        return 'Not Found!'

    def getStepTimers(self, title): # It returns a list
        for d in self.data:
            if title in d['name']:
                return d['timers']
        return 'Not Found!'

    def getImage(self, title): # It returns a list
        for d in self.data:
            if title in d['name']:
                return d['imageURL']
        return 'Not Found!'