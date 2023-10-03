"""
Problem
You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
"""

"""
Keeping a limited history is a perfect use for a collections.deque.
"""

"""
The yield statement suspends a function’s execution and sends a value back to the caller, 
but retains enough state to enable the function to resume where it left off. 
When the function resumes, it continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, rather than 
computing them at once and sending them back like a list.
"""

from collections import deque

def showcaseDeque():
    
    q = deque( maxlen = 3 )
    print( 'This is a simple deque:', q )
    print( '' )
    print( 'You can add elements to it' )
    q.append( 'one' )
    print( 'q =', q )
    q.append( 'two' )
    print( 'q =', q )
    q.append( 'three' )
    print( 'q =', q )
    print( '' )
    print( "Now that it's full. look what happens when we append a new element" )
    q.append( 'hey!' )
    print( 'q =', q )
    print( '' )
    print( 'You can append or pop elements from both right side or left side of the deque' )
    q.popleft()
    print( 'q =', q )
    print( '' )
    

def  searchAndDeque():
    
    def search( lines , pattern , history = 5 ):
    
        # declares a deque type object with a fixed max amount of elements
        previous_lines = deque( maxlen = history )
        
        for line in lines:
            if pattern in line:
                print( '*** yield point: ***' )
                print( 'line =', line )
                print( 'previous_lines =', previous_lines )
                print( '\n' )
                    
                yield line , previous_lines
                
            previous_lines.append( line )
    
    
    with open( 'somefile.txt' ) as f:
        for line, prevlines in search( f , 'python' , 5):
            print( '*** main function: ***' )
            print( 'line =', line )
            print( 'prevlines =', prevlines )
            #for prev_line in prevlines:
            #    print( prev_line )
            print( '-'*50 )
            print( '-'*50 )
            

# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Basic use of deque' )
        print( '( 2 ) Search and use deque to keep values' )
        print( '( 0 ) exit' )
        print( '---' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                showcaseDeque()
            case '2':
                searchAndDeque()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n'*2 )