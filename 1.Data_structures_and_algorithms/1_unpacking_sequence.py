"""
Problem: 
You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
"""

""" 
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
IMPORTANT: The number of variables to unpack into and elements to unpack must be the same.
"""
def unpackSimpleTuple():
    
    my_tuple  = ( 1 , 2 )
    x , y = my_tuple

    print( 'Unpacking my_tuple:' )
    print( 'my_tuple =' , my_tuple )
    print( 'x =' , x )
    print( 'y =' , y )


def unpackNestedTuple():

    my_tuple = ( 1, 2, 3, ( 'a' , 'b' , 'c') )
    x1 , x2 , x3 , x4 =  my_tuple
    x4_1 , x4_2 , x4_3 = x4
    
    print( 'Unpacking nested_tuple:' )
    print( 'my_tuple =' , my_tuple )
    print( 'x1 =' , x1 )
    print( 'x2 =' , x2 )
    print( 'x3 =' , x3 )
    print( 'x4 =' , x4 )
    print( 'x4_1 =' , x4_1 )
    print( 'x4_2 =' , x4_2 )
    print( 'x4_3 =' , x4_3 )


def unpackCertainItems():
    # _ notation states for values not to unpack
    
    my_tuple = ( 1, 2, 3, ( 'a' , 'b' , 'c') )
    _ , x2 , _ , x4 =  my_tuple
    x4_1 , _ , x4_3 = x4
    
    print( 'Unpacking certain elements from nested_tuple:' )
    print( 'my_tuple =' , my_tuple )
    print( 'x1 _' )
    print( 'x2 =' , x2 )
    print( 'x3 _' )
    print( 'x4 =' , x4 )
    print( 'x4_1 =' , x4_1 )
    print( 'x4_2 _' )
    print( 'x4_3 =' , x4_3 )
    
def unpackString():
    # Space counts as character
    
    s = 'My string'
    s1 , s2 , s3 , s4 , s5 , s6 , s7 , s8 , s9 = s
    
    print('Unpacking a string:')
    print( 's ='  , s )
    print( 's1 =' , s1 )
    print( 's2 =' , s2 )
    print( 's3 =' , s3 )
    print( 's4 =' , s4 )
    print( 's5 =' , s5 )
    print( 'You got the rest...' )


# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Unpack a simple tuple' )
        print( '( 2 ) Unpack a nested tuple' )
        print( '( 3 ) Unpack only certain items from a tuple' )
        print( '( 4 ) Unpack a string' )
        print( '( 0 ) exit' )
        print( '---' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                unpackSimpleTuple()
            case '2':
                unpackNestedTuple()
            case '3':
                unpackCertainItems()
            case '4':
                unpackString()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )