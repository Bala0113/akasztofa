 # Python haladó beadandó - Akasztófa  játék

 ## A játék lényege
Akasztófa  játék - Meg van adva egy szó hossza és tippelnünk kell hogy milyen betűk szerepelhetnek az adott szóban, ha van a szóban akkor az megjelenik, ha nem akkor vesztünk egy életet és elkezd kirajzolódni az akasztófa. 

 ## Indítása
A program indítása után a menü ablak ugrik fel, itt a játék gombra kattintva elindul a játék, a súgó gombra kattintva felugrik egy ablak a játék leírásáról.
A Játék indítása után a program legenerál egy szót, amelynek csak a hosszát látjuk. A Szöveg mezőbe egy betűt kell beütnünk majd a kész gombra kell nyomnunk.
A program a kész gomb megnyomására ellenőrzi hogy az adott szó tartalmazza-e azt a betűt, Ha igen az megjelenik a vonal helyén a beírt betű. Ha nem akkor az elvesztünk  egy életet és elkezd kirajzolódni az akasztófa. 
Minden egyes tipp után az ablak alján megjelenik az adott betű, mint felhasznált betű. Ezeket a betűkkel már nem próbálkozhatunk. Mind addig próbálkozhatunk, amíg ki  nem rajzolódik az akasztófa (13 lehetőség).
Ha a 13. próbálkozás után se tudtuk kitalálni a szót, akkor felugrik egy ablak "Vesztettél" felírattal és a kitalálandó szóval. Itt ok gombra kattintva bezárja a játékot.
Ha kitaláltuk a játékot akkor ugyanez történik "Nyertél" felírattal.

 ## Függvények működése
> - **home():** Létrehozza a main ablakot 2 gombbal + szöveggel a newGameButton-ra kattintva -> startGame()
> - **startGame()**: törli a main ablakot + letterList-be betűnként lementi a randomWord() +  Létrehozza a gamePage ablakot, szövegmezővel, szövegekkel, képpel, gombbal= check() + emptyList(vonalak) + usedLetter(használt betűk)
> - **randomWord():** a szavak.txt fájlból kiválaszt egy szót és azt adja vissza
> - **check():** A szövegmezőből kimenti a betűt, ellenőrzi a formátumát + letterChek indexei alapján ellenőrzi a tippet. Ha talál a szóban: usedLetter-hez és emptyList-hez hozzáadja a betűt + winCheck. Ha nem talál -1health, + animation() + ha health=0 -> gameOver()
> - **letterChek**: megkapja a betűt, végig fut a word-ön, vissza ad egy listát az indexekről, amelyben a betű helyét tárolja.
> - **winCheck**: összehasonlítja az emptyList és letterList elemeit, ha megegyeznek ->win() 
> - **animation()**: összerakja a health segítségével a fájlnevet (image1 -> image13) majd képernyőre dobja
> - **gameOver() + win()**: feldob egy ablakot, kilép
