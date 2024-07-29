#just a class where the spam phrase will be stored
class spamPhrase():

  #class will be initialized with the phrase to be spammed
  #object should be created with phrase as a parameter
  def __init__(self, phrase):
    self.phrase = phrase
    
  #in case you want to change the phrase quickly without having to create a new object. 
  def changePhrase(self, nPhrase):
    self.phrase = nPhrase
  #method to get phrase to a variable
  def getPhrase(self):
    return self.phrase