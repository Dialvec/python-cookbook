"""
Problem
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements
"""

"""
Python "start expressions" gathers all unpacked values from the position it is declared up to:
- The declaration of trailing variables to unpack into
- The end of the iterable's values

Star value stores all the values into a list, even if it does not contain any data
"""

def unpackTrailValues():
    
    user_data = ( 'John Doe' , 'jhon_doe@mail.com' , '123-456-7879' , '+1-111-222-3456' )
    name , email , *phone_numbers = user_data
    
    print( 'Unpacking user_data:' )
    print( 'user_data =' , user_data )
    print( 'name ='  , name  )
    print( 'email =' , email )
    print( '*phone_numbers =' , phone_numbers )
    print( "*phone_numbers' type =", type( phone_numbers ) )
    

def unpackLeadValues():
    
    values = ( 1 , 2 , 3 , 4 , 5 )
    *lead_values , last_value = values
    
    print( 'Unpacking values:' )
    print( 'values =' , values )
    print( '*lead_values =' , lead_values )
    print( 'last_value ='   , last_value  )



"""
You can pass use unpacking to get specific values, decide based on them and pass the rest of the
unpacked values to specialized functions.

Note we passed the packed *args as a list. If we pass non-starred args, the function 
will recieve each unpacked value as an individual argument like greetUser( arg_1 , arg_2 , ... , arg_n )

Also note we unpack phone_numbers in the print statement so each phone number is treated as an individual value,
equivalent to print( 'Or call you to' , phone_number_1 , phone_number_2 , ... , phone_number_n )
"""
def unpackDecideExcecute():
    records = [
        ( 'user' , 'John Doe' , 'jhon_doe@mail.com' , '123-456-7879' , '+1-111-222-3456' ),
        ( 'sqr'  , 42 ),
        ( 'Hello', 'a', 'b', 'c' ),
        ( 'user' , 'Bruce Wayne' , 'im_not_batman@batman.com' ),
        ( 'sqr'  , 100 )
    ]
    
    def greetUser( *args ):
        name , email , *phone_numbers = args
        
        print( 'Greetigs dear' , name )
        print( 'We will contact you at' , email )
        
        if len( phone_numbers ) > 0 :
            print( 'Or call you to' , *phone_numbers )
        
    
    def computeSqr( x ):
        print( 'Squared value of', x, 'is', x*x )
        
        
    for tag, *args in records:
        
        print( 'Current tuple:' , ( tag, *args ) )
        
        if tag == 'user':
            greetUser( *args )
        elif tag == 'sqr':
            computeSqr( *args )
        else:
            print( 'No operation defined for tag:', tag )
        
        print('')
            

def unpackString():
    line = 'batman:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    
    print( 'Unpacking String by delimiter ":" ' )
    print( 'line  ='  , line    )
    print( 'uname ='  , uname   )
    print( '*fields =', fields  )
    print( 'homedir =', homedir )
    print( 'sh ='     , sh      )
    


def unpackAndThrowAway():
    
    user_data = ( 'John Doe' , 'jhon_doe@mail.com' , '123-456-7879' , '+1-111-222-3456' , ( 17 , 12 , 1990 ))
    name , email , *_ , ( *_ , year) = user_data
    
    print( 'Unpacking and throwing away data:' )
    print( 'user data =' , user_data )
    print( 'name ='  , name  )
    print( 'email =' , email )
    print( 'last ignored pack:' , _    )
    print( 'year ='   , year )


# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Unpack trailing values' )
        print( '( 2 ) Unpack lead values' )
        print( '( 3 ) Unpack, decide and execute functions' )
        print( '( 4 ) Unpack a string' )
        print( '( 5 ) Unpack and throw values away' )
        print( '( 0 ) exit' )
        print( '---' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                unpackTrailValues()
            case '2':
                unpackLeadValues()
            case '3':
                unpackDecideExcecute()
            case '4':
                unpackString()
            case '5':
                unpackAndThrowAway()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '' )
        print( '-'*50 )
        print( '\n' )