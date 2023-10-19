"""
Problem
You want to make a list of the largest or smallest N items in a collection.
"""

"""
The heapq module has two functions—nlargest() and nsmallest().
Heap work by first converting the data into a list where items are ordered as a heap.
The most important feature of a heap is that heap[0] is always the smallest item.
"""

import heapq

def heapifyList():
    
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    
    heap = nums.copy()
    
    heapq.heapify( heap )
    
    print( 'nums =' , nums )
    print( 'heap =' , heap )
    print( '' )
    print( 'We can pop the smallest item of the heap:' )
    print( '' )
    print( 'heapq.heappop( heap ) ->' , heapq.heappop( heap ) )
    print( 'heap =' , heap )
    print( '' )
    print( 'heapq.heappop( heap ) ->' , heapq.heappop( heap ) )
    print( 'heap =' , heap )
    


def getNExtremeValues():
    
    values = [ 1 , 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 ]
    
    n_smallest = heapq.nsmallest( 3 , values )
    n_largest  = heapq.nlargest(  3 , values )
    
    print( 'values =' , values )
    print( 'Smallest values =' , n_smallest )
    print( 'Largest values ='  , n_largest )


def getNExtremeFromDict():
    
    portfolio = [
        {'name': 'IBM'  , 'shares': 100 , 'price': 91.1   },
        {'name': 'AAPL' , 'shares': 50  , 'price': 543.22 },
        {'name': 'FB'   , 'shares': 200 , 'price': 21.09  },
        {'name': 'HPQ'  , 'shares': 35  , 'price': 31.75  },
        {'name': 'YHOO' , 'shares': 45  , 'price': 16.35  },
        {'name': 'ACME' , 'shares': 75  , 'price': 115.65 }
    ]
    
    def getStockPrice( stock = dict ):
        return( stock["price"] )
    
    n_cheapest  = heapq.nsmallest( 3 , portfolio , key = getStockPrice )
    n_expensive = heapq.nlargest(  3 , portfolio , key = getStockPrice )
    
    print( 'portfolio =' , portfolio )
    print( 'Cheapest stocks ='        , n_cheapest  )
    print( 'Most expensive stocks ='  , n_expensive )

# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Heapify a list of numbers' )
        print( '( 2 ) Get the highest and smallest values' )
        print( '( 3 ) Sort list of dictionaries by a specific key value ' )
        print( '( 0 ) exit' )
        print( '---' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                heapifyList()
            case '2':
                getNExtremeValues()
            case '3':
                getNExtremeFromDict()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n'*2 )