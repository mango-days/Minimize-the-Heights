# Minimize the Heights

# Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 

# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

height = [ 1, 5, 8, 10 ]
k = 2

for index in range ( 0 , len ( height ) ) :
    if height [ index ] >= k : height [ index ] -= k
    else : height [ index ] += k
    height [ index ] = int ( height [ index ] )
    
max_diff = max ( height ) - min ( height )
print ( max_diff )
