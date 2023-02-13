import random
from tkinter import *
from tkinter import ttk, messagebox

''' Megszáolja a szöveges fájl sorait, majd 0 és a sorokszáma között generál egy random számot. 
    És azt a szót választja, ahol generált szám megegyezik a sorának számával.'''


def randomWord():
    with open(r'szavak.txt') as fp:
        for count, line in enumerate(fp):
            pass
    return open(r'szavak.txt').readlines()[random.randint(0, count)]


''' Elindul a játék'''


def startGame():
    global main
    main.destroy()
    global health
    health = 13
    word = randomWord()

    """Játék vége"""

    def animation(health):
        fileName = "image" + str(14 - health) + ".png"
        im = PhotoImage(file=fileName)
        Label(gamePage, image=im).place(x=28, y=0)
        gamePage.mainloop()

    def gameOver():

        messagebox.showerror("Vesztettél", "Vesztettél! A szó a/z " + word + "volt")
        gamePage.destroy()
        exit()

    """Játék vége"""

    def win():
        messagebox.showinfo(title='Nyertél', message='Nyertél! A szó a/z ' + word + ' volt')
        gamePage.destroy()
        exit()

    """Ellenőrzi a két lista elemeit (letterList,emptyList), ha ugyanazok akkor nyert a játékos"""

    def winCheck():
        correctLetter = 0
        counter = 0
        for x in letterList:
            if letterList[counter] == emptyList[counter]:
                correctLetter += 1
                counter += 1
            else:
                break
        if correctLetter == len(word) - 1: win()

    """Végig megy a azon lista elemein(a betűkön), amely a kitalálando szót tartalmazza, és összeveti a beírt betűvel 
        ---> egy listát ad vissza amely tartalmazza az azonos betűk indexét"""

    def letterCheck(letter):
        indexList = [-1]
        result = word.find(letter)
        i = 0
        while True:
            if result > -1 and result != indexList[0]:
                indexList.append(result)
                result1 = result + 1
                result = word.find(letter, result1)
                i += 1
            else:
                return indexList

    """A letterChecket használva kiíatja az eltalált betűket a képernyőre, ha van benne olyan betű, +winCheck.
        Ha nem talált el egy betüt sem akkor levon egy életet. +betű a usedList-be"""

    def check():

        e_letter = e1.get()
        if e_letter.isalpha() and len(e_letter) == 1 and e_letter not in usedLetter:
            index = letterCheck(e_letter)
            if (len(index)) > 1:
                index.remove(-1)
                k = 0
                for x in index:
                    emptyList[index[k]] = e_letter
                    k += 1
                mainLabel = Label
                mainLabel(gamePage, text=emptyList,
                          font=("Courier", 30)).place(x=25, y=320)
                usedLetter.append(e_letter)
                Label(gamePage, text=usedLetter,
                      font=("Arial", 12)).place(x=15, y=550)
                winCheck()

            else:
                global health
                health -= 1
                Label(gamePage, text='Próbálkozások száma: \n' + str(health),
                      font=("Arial", 12)).place(x=15, y=450)
                usedLetter.append(e_letter)
                Label(gamePage, text=usedLetter,
                      font=("Arial", 12)).place(x=15, y=550)
                if health == 0: gameOver()
                animation(health)
        else:
            messagebox.showerror("Hibás bemenet!",
                                 "Csak 1 karakter hosszú betűt adhasz meg, amit még nem használtál fel!")

    """A szó listába mentése betűnként"""
    letterList = []
    for letter in word:
        letterList.append(letter)
    del letterList[-1]

    """ablak létrehozása"""
    gamePage = Tk()
    gamePage.geometry('360x600')
    gamePage.resizable(width=False, height=False)
    gamePage.title('Akasztófa - YCWCAZ')

    """INTERFACE"""
    tipLabel = Label(gamePage, text='Tipp: ')
    tipLabel.place(x=75, y=375)
    letter = StringVar(gamePage)
    e1 = Entry(gamePage, textvariable=letter)
    e1.place(x=35, y=400)
    Label(gamePage, text='Próbálkozások száma: \n' + str(health),
          font=("Arial", 12)).place(x=15, y=450)
    usedLetter = []
    Label(gamePage, text='Felhasznált betűk:',
          font=("Arial", 12)).place(x=15, y=530)

    """Ellenőrző gomb"""
    button = ttk.Button(gamePage, text="Kész", command=check)
    button.pack()
    button.place(x=180, y=397)
    """Üres lista létrehozás '_' használva és kiiratása"""
    emptyList = []
    x = 1
    while x < len(word):
        emptyList.append('_')
        x += 1

    Label(gamePage, text=emptyList,
          font=("Courier", 30)).place(x=25, y=320)

    """Akasztófa"""
    im = PhotoImage(file="image1.png")
    hatter_label = Label(image=im)
    hatter_label.place(x=0, y=0)
    hatter_label.pack()

    gamePage.mainloop()


"""Menü ablak"""


def home():
    """main = Tk()"""
    global main
    main.geometry('360x150')
    main.resizable(width=False, height=False)
    main.title('Akasztófa menü - YCWCAZ')
    Label(main, text='A játékot készítette: Mihalovics Balázs',
          font=("times", 16, 'italic')).place(x=19, y=110)
    description = 'A kitalálandó szót a szóban szereplő betűk számával megegyező számú és elrendezésű vízszintes ' \
                  'vonalreprezentálja. A  játékos javasol egy betűt, mely ha szerepel a kitalálandó szóban, ' \
                  'a betű helyének megfelelő vonalakra ráírásra kerül. Amennyiben a betű nem szerepel a kitalálandó ' \
                  'szóban, úgy egy stilizált akasztófa egy része kerül lerajzolásra. '
    newGameButton = ttk.Button(main, text="Játék", command=lambda: startGame())
    newGameButton.pack()
    newGameButton.place(x=150, y=30)
    newGameButton = ttk.Button(main, text="Súgó",
                               command=lambda: messagebox.showinfo(title=None, message=str(description))())
    newGameButton.pack()
    newGameButton.place(x=150, y=60)
    main.mainloop()


"""BEGINNING"""
main = Tk()
home()
health = 0
