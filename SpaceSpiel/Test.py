
def test (x) :
    testNum = True
    if x == 3 :
        testNum = False
    return testNum
def wieder(value) :
    while True :
        if test(value) == False :
            break
        else :
              value = int(input("please Enter the Number 3 : "))

def maintest ():
     Xint = int(input("please Enter the Number 3 : "))
     wieder(Xint)

maintest()










# password = input("please enter your password : ")
# while True :
#     if password == "123" :
#         print("hallo Abdul")
#         break
#     else :
#         password = input("please enter your password : ")
