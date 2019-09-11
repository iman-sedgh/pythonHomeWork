print 'started'

EvenNumber = 1
OddNumber = 0
while EvenNumber%2 != 0:
        print 'Please Enter an Even (ZOj)  Number'
        EvenNumber = int( raw_input() ) 
     
#print 'Your Number Is ',firstnumber
counter = EvenNumber
while counter > 0 :
    
    
    while OddNumber%2 !=1 :  
        print EvenNumber-(counter-1),': Now Enter an Odd (Fard) Number'    
        OddNumber = int( raw_input() ) 
    #neveshtan adad va kam kardan
    while OddNumber >= 1 :
        print 'Odd Number :',OddNumber
        OddNumber -= 2
    OddNumber = 0
    counter -= 1    
#    print 'another loop'

print 'End of the program'    
    
    
