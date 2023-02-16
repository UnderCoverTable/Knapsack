def KnapSack(MaxW,itemV,itemW,items,A,B): ## --> O(n*W)
    
    # Base Case
    if items == 0:
        return 0
    if MaxW == 0:
        return 0

    if itemW[items-1] > MaxW: #Item weight greater then total capacity
        if A[items - 1][MaxW] is None:
            A[items - 1][MaxW] = KnapSack(MaxW,itemV,itemW,items-1,A,B)
        
        return A[items - 1][MaxW] # Value of the immediate upper neighbour


    else: #Items weight is within capacity
        if A[items - 1][MaxW] is None:
            A[items - 1][MaxW] = KnapSack(MaxW,itemV,itemW,items-1,A,B) 

        if A[items - 1][MaxW - itemW[items-1]] is None:
            A[items - 1][MaxW - itemW[items-1]] = KnapSack(MaxW-itemW[items-1],itemV,itemW,items-1,A,B) 

                    # Value if item isnt picked           # Value if item is picked
        maxx = max(A[items - 1][MaxW] , itemV[items-1] + A[items - 1][MaxW - itemW[items-1]]) 

        if maxx == itemV[items-1] + A[items - 1][MaxW - itemW[items-1]]:
            B[items][MaxW] = True # Updates the boolean table to show that the item was picked up

        return maxx


def fill_table(MaxW,itemV,itemW,items,A,B): ## o(n^2 + n) 

    # Fills up the rest of the empty cells in the 2d array A. 
    for i in range(items+1): ## --> n^2
        for j in range(MaxW+1):

            if i == 0 or j == 0:
                A[i][j] = 0
            
            
            if A[i][j] is None:
                A[i][j] = KnapSack(j,itemV,itemW,i,A,B) ## --> o(n*W)

    # Uses 2d Array B to print out what items were picked and which werent
    k = MaxW
    w_used = 0
    for i in range (items,-1,-1): ## --> n
        
        if B[i][k] is True: # Item was picked
            
            w_used += itemW[i-1]
            k = k - itemW[i-1]
            print("Item",i, "was picked.", "  ->  [Value=",itemV[i-1],": Weight=",itemW[i-1],"]")
        else:
            if i !=False: # Item was not picked
                print("Item",i, "was not picked.")
                
    print("\nMax value: ", A[items][MaxW], " - Weight used: ",w_used, " - Remaining Capacity: ",k)
    



value = [4,6,9] # List of the values of items
weight = [4,3,5] # List of the weights of items
total_capacity = 10 # Capacity of the sack
total_items = len(value) # Number of items in the store

A = [[None for x in range(total_capacity + 1)] for x in range(total_items + 1)] # Initialise 2d array to hold all the values
B = [[False for x in range(total_capacity + 1)] for x in range(total_items + 1)] # Initialise 2d array to hold boolean values of whether an item was picked or not

## o(n*W)
KnapSack(total_capacity, value, weight, total_items, A, B) # Initially fills the table partially

## o(n^2) 
fill_table(total_capacity, value, weight, total_items, A, B) # Fills the table up then prints what items were chosen



def print_matrix(A):
	for i in range(len(A)):
			print(A[i])

print_matrix(A)
#print_matrix(B)
