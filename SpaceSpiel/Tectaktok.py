feld=[ 1 ,"|", 2 ,"|", 3 ,
       4 ,"|", 5 ,"|", 6 ,
       7 ,"|", 8 ,"|", 9
      ]
feldtest=[ None ,"|",None  ,"|", None ,
           None ,"|", None ,"|", None ,
           None ,"|", None ,"|", None
      ]
def printfeld():
    for i in range(0,len(feld)):
        print(feld[i],end=" ")
        if i == 4 or i == 9 :
            print()


def eintragenSpiel1(value):
    Andere_Ein = True
    if value in feldtest :
        print ("bitte geben Sie andere Nummer ein, die Nummber ist schon ausgewählt ")
        Andere_Ein = False
    else :
          for e in range(0, len(feld)):
              if (feld[e] == value) :
                   feld[e] = "X"
                   feldtest[e] = value
    return Andere_Ein
def eintragenSpiel2(value):
    Andere_Ein = True
    if value in feldtest:
        print("bitte geben Sie andere Nummer ein, die Nummber ist schon ausgewählt ")
        Andere_Ein = False
    else:
        for e in range(0, len(feld)):
            if (feld[e] == value):
                feld[e] = "O"
                feldtest[e] = value
    return Andere_Ein

def gewinn_spiel1(feld):
        gewinn = False
        if (feld[0] == "X" and feld[2]=="X" and feld[4]=="X" )  or (
            feld[5] == "X" and feld[7] == "X" and feld[9] == "X") or (
            feld[10] == "X" and feld[12] == "X" and feld[14] == "X") or (
            feld[0] == "X" and feld[5] == "X" and feld[10] == "X") or (
            feld[2] == "X" and feld[7] == "X" and feld[12] == "X") or (
            feld[4] == "X" and feld[9] == "X" and feld[14] == "X") or (
            feld[0] == "X" and feld[7] == "X" and feld[14] == "X") or (
            feld[4] == "X" and feld[7] == "X" and feld[10] == "X"):
            gewinn = True
        return gewinn

def gewinn_spiel2(feld):
     gewinn = False
     if(    feld[0] == "O" and feld[2] == "O" and feld[4] == "O") or (
            feld[5] == "O" and feld[7] == "O" and feld[9] == "O") or (
            feld[10] == "O" and feld[12] == "O" and feld[14] == "O") or (
            feld[0] == "O" and feld[5] == "O" and feld[10] == "O") or (
            feld[2] == "O" and feld[7] == "O" and feld[12] == "O") or (
            feld[4] == "O" and feld[9] == "O" and feld[14] == "O") or (
            feld[0] == "O" and feld[7] == "O" and feld[14] == "O") or (
            feld[4] == "O" and feld[7] == "O" and feld[10] == "O"):
            gewinn = True

     return gewinn

def spiel_exit(feldtest):
    weiter = False
    value = None
    if value in feldtest :
        weiter = True
    return weiter



def mainsspiel():
    Folge = False
    Spielnum = 1
    while True :
          printfeld()
          print("")
          element1 = int(input(f"Spieler {Spielnum} wählen Sie bitte ein gewünschte Zelle (Nummer) aus : "))
          if element1 >=10 or element1 <=0 :
            print ("bitte geben Sie eine Zahl vom dargestellten Feld ein ")
            continue
          elif Folge == False :
                andere_Zahl = eintragenSpiel1(element1)
                if andere_Zahl == False :
                   continue
                else :
                    Folge = True
                    Spielnum = 2
                if gewinn_spiel1(feld) == True :
                   print("Spieler 1 hat gewonnen ")
                   printfeld()
                   print("")
                   break
          else :
           andere_Zahl = eintragenSpiel2(element1)
           if andere_Zahl == False:
               continue
           else :
               Folge = False
               Spielnum = 1
           if gewinn_spiel2(feld) == True:
               print("Spieler 2 hat gewonnen ")
               printfeld()
               print("")
               break

          if spiel_exit(feldtest) == False :
             print ("Das Ergebnis ist gleich , niemand hat gewonnen ")
             printfeld()
             print("")
             break
          else :
             continue
mainsspiel()
