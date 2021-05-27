#!/usr/bin/env python3

def  getData( index ):
    data = [ 10, 20, 30, 40, 50 ]
    return data[index]
try:
    index = int( input( "Enter an index: >>> " ))
    print( f"Data with index nr. <{index }> = {getData( index )}" )
except:
    print( "ValueError: the entered value does not valid! " )

index = 1000
try:
    print( getData( index ))
except:
    print( "Error! Index aut of range!" )
