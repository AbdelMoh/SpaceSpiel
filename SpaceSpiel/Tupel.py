# def infos():
#     person = ("Sibel","Yigitoglu",31)
#     return person
#
# print(infos())
def multi(num1,num2,*num):
    sum = num1 * num2
    m = 4
    for i in num :
        sum *=i
    return sum


m = 3
print (m)
# print(multi(1,2,3))