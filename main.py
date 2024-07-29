from distutils import command
from threading import Thread
from time import sleep
from tkinter import font, messagebox
from spam import spammer
from phrase import spamPhrase
from tkinter import *
from PIL import Image, ImageTk

'''
  s.locateTarget()
  input()
  s.sendPhrase(p)
  '''

#UI generation
def spamGUI():
  global window
  #window proportions
  window = Tk()
  window.title("SpamBot")
  window.geometry("720x480")
  #canvas creation for the image
  canvas = Canvas(window, width=300, height=300)
  canvas.pack()
  #storing and resizing the image
  img = Image.open("utils/Logo.png")
  img = img.resize((200,200), Image.ANTIALIAS)

  img = ImageTk.PhotoImage(img)
  #displaying the image
  canvas.create_image(50,20, anchor=NW, image=img)

  #Creating the text labels just indicating to insert information
  l = Label(window, text= "Select Contact to be Spammed", font="none 11")
  l.place(relx= .10, rely= .50, anchor='w')

  l = Label(window, text= "Type in Phrase", font="none 11")
  l.place(relx= .70, rely= .50, anchor='e')
  

  #creating the textboxes where the user will input their stuff
  global e, e2
  e = Entry(window, width=25)
  e2 = Entry(window, width=25)
  e.place(relx= .10, rely= .55, anchor='w')
  e2.place(relx= .77, rely= .55, anchor='e')

  #The button that will begin it all, REMEMBER TO NULLIFY IT SOMEHOW WHILE THE FUNCTION IS RUNNING. 
  global button_start
  button_start = Button(window, text="Begin Spam", padx=10, pady=10, command= lambda:openWindow())
  button_start.place(relx=.45, rely= .75, anchor= 'center')
  
  #Instructions
  #messagebox.showinfo("Instructions", "These will be Instructions")
  window.mainloop()
  
#this method will only focus up to the scanning portion
#MAKE SURE TO HAVE ALL THE PROCESS IN THE ERROR CATH
def openWindow():
  #retrieve information from text boxes (Remember to implement logic for wrong inputs)
  name = e.get()
  phrase = e2.get()
  #shut down the textboxes while the program is running (be sure to implemente a reactivation when reset)
  e.configure(state="disabled")
  e2.configure(state = "disabled")
  button_start.configure(state="disabled")
  #spammer and phrase instances, webdriver is also instanciated. 
  global s
  global p
  s = spammer(name)
  p = spamPhrase(phrase)

  #a new continue button is added to pause the program so the user has time to scan the whatsapp thing
  #(implement logic to make sure the program continues only after the user has done a real scan)
  b = Button(window, text="Continue", command=lambda: locate(b))
  #button_quit = Button(window, text="Quit", command=lambda: reset(s, b, button_quit))
  
  
  #test logic for incorrect inputs
  if(name != ''):
    b.place(relx=.65, rely= .65, anchor= 'center')
    #button_quit.place(relx=.65, rely= .75, anchor= 'center')
    print(name + " " + phrase)
    print(type(name))
    
  else:
    messagebox.showerror("Error", "The name should have some kind of value in it")
    print("name should be filled")

  #run my fancy little code up to the scan
  s.login()
  

#does what it says, after user scans and presses button, program will continue and find the target
#Spam will also be implemented in this function, however make sure to add a quit button
#quit button will not only terminate the spam but it should reset the GUI to its original state
def locate(*args: Button):
  if(len(args) == 0):
    if(s.isFalse() == True):
      s.changeTarget(e.get())
      global p
      p.changePhrase(e2.get())
      e.configure(state="disabled")
      e2.configure(state="disabled")
      s.locateTarget()

      button_spam = Button(window, text="Spam", command=lambda: Thread(target= sendMessages).start())
      button_quit = Button(window, text="Quit", command=lambda: reset(button_spam, button_quit))
      
      button_spam.place(relx=.65, rely= .60, anchor= 'center')
      button_quit.place(relx=.65, rely= .70, anchor= 'center')
      
    else:
      pass
  else:
    if(s.isFalse() == True):


      s.locateTarget()
      args[0].place_forget()
      
      button_spam = Button(window, text="Spam", command=lambda: Thread(target= sendMessages).start())
      button_quit = Button(window, text="Quit", command=lambda: reset(button_spam, button_quit))
      
      button_spam.place(relx=.65, rely= .60, anchor= 'center')
      button_quit.place(relx=.65, rely= .70, anchor= 'center')
      
    else:
      pass
  

  


def reset(b:Button, b2: Button, ):
  s.onStop()
  b.place_forget()
  b2.place_forget()
  button_start.configure(state="active", command= lambda: locate())
  e.configure(state="normal")
  e2.configure(state="normal")
  




def sendMessages():
  s.sendPhrase(p.getPhrase())

#annoying main shit
def main():
  spamGUI()
  
  

if __name__ == "__main__":
  main()



