# I used fuction I learned fron the Tuesday class
def num(total_money,price):   #define the function
    number=total_money//price #determine the number of bought chocolate
    left=total_money%price    #determine the money left
    return number,left
tot_money=input()
pri=input()
result=num(int(tot_money),int(pri))
print(result[0],result[1])
# I use 20 3 for example
#the results were'6 2'
