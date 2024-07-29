#this is the file that will do all the fun browser stuff
#import selenium for browser and phrase for spam reference
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import msvcrt


#create driver as a global so we can access it in all methods
global driver

#our spammer class which will have our step by step methods to accessing our target
class spammer():
  
  #our object will be initialized with the name of the target to be spammed
  #argument should be whatever name is saved in the users (currently only),  whatsapp
  #will also initialize the driver
  def __init__(self, target):
    self.target = target
    print("Target accepted " + target)
    #path is where the chromedriver is stored, keep in mind for other machines
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    self.driver = webdriver.Chrome(PATH)

    self.onStop()


  def changeTarget(self, ntarget):
    self.target = ntarget


  #a method to open a browser to whatsapp
  def login(self):
    driver = self.driver
    #opens the website
    driver.get("https://web.whatsapp.com")

    #whatsapp requires a scan by force, so the user should be ready to scan
    print("You should probably scan your thing now, press enter once you are properly logged in")

    #this input is only here to freeze the process until user can can, will try to add a button or something
    #in the GUI
    #input()

  #once whatsapp is opened this method will find the user to be spammed
  def locateTarget(self):
    #name of contact
    t = self.target
    #global driver
    driver = self.driver

    #xpath that finds the new chat button
    xpath = '//*[@id="side"]/header/div[2]/div/span/div[2]/div'
    #finding the element with our search condition
    search = driver.find_element_by_xpath(xpath)
    #you should be able to figure this out, it clicks it @.@
    search.click()

    #xpath for the search bar within the new chat
    xpath = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
  
    #find the search based off the xpath
    search = driver.find_element_by_xpath(xpath)
    #sending the name of the contact to the search
    search.send_keys(t)
    sleep(1)
    #locate literally the only contact, but specific search just in case
    xpath = '//*[@title = "{}"]'.format(t)
    search = driver.find_element_by_xpath(xpath)
    #finally clicking into the contact @.@
    search.click()
    global keyboard
    driver = self.driver
    xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    keyboard = driver.find_element_by_xpath(xpath)
    

  def sendPhrase(self, phrase):
    #do not run the cycle yet, check basic messages first
    #dont worry past Matt, it works
    self.onStart()
    while running == False:
      keyboard.send_keys(phrase + Keys.ENTER)
      
    
    
    print('we out')

  



  def onStart(self):
    global running
    running = False

    
    
  def onStop(self):
    global running
    running = True

  def isFalse(self):
    global running
    return running

  def quitBrowser(self):
    self.driver.quit()


#change method name on the thread, sender not locator. 




