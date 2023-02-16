
def print_matrix(A):
	for i in range(len(A)):
			print(A[i])

def KnapSack(Max_w,Item_w,Item_vals,n_items):

    A = [[None for x in range(Max_w + 1)] for x in range(n_items+1)]
    B = [[False for x in range(Max_w + 1)] for x in range(n_items+1)]

    for i in range(n_items+1):
        for j in range(Max_w+1):
         
            if i == 0 or j == 0:
                A[i][j] = 0

        
            if A[i][j] is None:
                if Item_w[i-1] > j:  # Cant pick
                    A[i][j] = A[i-1][j]

                else:
                    max_val = max( A[i-1][j] , Item_vals[i-1] + A[i-1][j-Item_w[i-1]] )
                    A[i][j] = max_val

                    if max_val != A[i-1][j]:
                        B[i][j] = True

    k = Max_w
    for i in range (n_items,-1,-1):
        if B[i][k] is True:
            print(i," Item was picked")
            k = k - Item_w[i-1]
        else:
            if i !=0: print(i," was not picked")

            
    return A,A[n][W],B


    
                    

val = [1000,500,200]#[1,6,18,22,28]
wt = [1,2,3]#[1,2,5,6,7]
W = 5
n = len(val)
#KnapSack(W, wt, val, n)[0]
print(KnapSack(W, wt, val, n)[1])
#print_matrix(KnapSack(W, wt, val, n)[2])