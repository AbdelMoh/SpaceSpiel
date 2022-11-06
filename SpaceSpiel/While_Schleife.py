Counter = 3
while Counter < 7 :
     print("Das ist die Aufgabe ......")
     Counter += 1

password = "password123"
username = ""
Counter = 3
print("Passen Sie auf , Sie haben nur DREI Versuche ")
while username != password and Counter >= 1 :
    username = input("Bitte geben Sie Ihr korreckte Passwort  : ")
    if username == password :
        break
    else:
       Counter -= 1
       print (f"Sie haben nur {Counter} Versuch")
if Counter < 1 :
    print("Das Konto wird gesperrt")
else :
    print("Die Aufgabe wurde erfolgreich geschafft ")
counter = 2
while counter < 4 :
    print(f"Die Anzahl ist: {counter} ")
    counter +=1
else :
    print("Die Aufgabe wurde erledigt ")