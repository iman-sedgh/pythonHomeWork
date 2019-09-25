#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:17:33 2019

@author: imansedgh
"""
# 4/4 Table 
""" 
     1   2   3    4
------------------------
1  |  *   -   -   -  
   | 
2  |  -   -   -   -  
   | 
2  |  -   -   -   -
   |
4  |  -   -   -   -
-------------------------
     1   2   3   4
"""
position = [1,1] #means 1/1 This is the defualt position 




while 1:

    availableMovements = [ [] , [] ] # [ [ x ] , [ y ] ]
    print 'current position :\n \t x--> ' + str( position[0] ) + '\n \t y--> ' + str( position [1] )
    print '\t ' + str ( position ) 
    # calculate the available movemants
    i = 1
    while i >= 0:
        availableMovements[i].append( position[i] )
        if  ( position[i] + 1 <= 4 ):
            availableMovements[i].append( position[i] + 1  )
            
        if ( position[i] - 1 >= 1):
            availableMovements[i].append ( position[i] - 1 )
        i -= 1 
                # Perfecto 

    finalavailableMovements = []
    
    for x in availableMovements[0] : # X ha
        for y in availableMovements[1]: # Y ha 
            finalavailableMovements.append ( [ x , y ] )
    print 'Enter ID of -> Available Movements :\n\t\t   ',
    print finalavailableMovements
    print '\t\t       0\t1\t2 \t3\t4\t5\t6\t7\t8'
    choice = int(raw_input( "Enter One of the IDs : " ) )
    position[0] = finalavailableMovements[choice][0]
    position[1] = finalavailableMovements[choice][1]
#print position











