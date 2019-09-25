Number = int (raw_input("Enter A Number: " ))
star =1 
space = Number/2
originalNumber = Number
while Number > originalNumber/2 :
    print ' '*space + '*'*star
   # print '*'*star
    star +=2
    space -= 1
    Number -=1
# OK , Hala BarAx ----->
star = originalNumber
space = 0 
while Number > 0 :
    Number -=1 
    star -=2
    space +=1
    print ' '*space + '*' * star
    
    
    

    
    