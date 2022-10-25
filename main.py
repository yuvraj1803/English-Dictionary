'''Members of the project
    => Yuvraj Sakshith
    => Rishon Joseph
    => Roshin Thomas
'''

from tkinter import *
from PyDictionary import PyDictionary
from functools import partial
import webbrowser
import requests
from bs4 import BeautifulSoup

def synonyms(term):  # this function returns a list of synonyms of the given word
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]


backClr = "#CFDEE3"


def googleMeaning(word):
    url = "https://www.google.com/search?q={}".format(word)
    webbrowser.open_new_tab(url)


def printSynonyms(word):
    syn = synonyms(word)  # syn is the list which is storing all the synonyms of the given word
    for i in syn:
        ll.config(text="Synonym: " + i, font=("Times", 25), background=backClr)


def printMeaning():
    word = inputSpace.get(1.0, "end-1c")
    dict = PyDictionary(word)
    googleButtonYes = Button(window, text='Yes', command=partial(googleMeaning, word))
    if (dict.meaning(word) == None):
        lb.config(text="Word not found! Try Again! :). Do You Want Me To Google This Word?", font=("Helvetika", 25))
        googleButtonYes.pack()
        return
    mean = dict.meaning(word)['Noun'][0]
    lb.config(text=word + ": " + mean, font=("Times", 25), background=backClr)
    printSynonyms(word)


window = Tk()
window.configure(background=backClr)
window.title("PES University's English Dictionary")
# windowIcon = PhotoImage(file = 'pesu-logo-seo.png')
# window.iconphoto(False,windowIcon)
window.geometry("1100x500")

inputSpace = Text(window, width=20, height=1, font=("Helvetika", 20))
inputSpace.pack(pady=20)

findButton = Button(window, text='Search', command=printMeaning, highlightcolor="blue")
findButton.pack()

lb = Label(window, text="", background=backClr)
lb.pack()
ll = Label(window, text="", background=backClr)
ll.pack()

window.mainloop()

