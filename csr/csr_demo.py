import numpy as np 
import time

values = [11, 12, 14, 22, 23, 25, 31, 33, 34, 42, 45, 46, 55, 65, 66, 67, 75, 77, 78, 87, 88, None]
row_pointer = [0, 3, 6, 9, 12, 13, 16, 19, 21, None, None, None, None, None, None, None, None, None, None, None, None, None]
columns = [0, 1, 3, 1, 2, 4, 0, 2, 3, 1, 4, 5, 4, 4, 5, 6, 4, 6, 7, 6 , 7, None]

def csr_reconstruction(values, columns, row_pointer, m, n):
	''' 
	Reconstructs a matrix from a compressed sparse row representation.  
	
	Args:  
		values: an array of nonzero index values
		columns: an array of column indices corresponding each value in values 
		row_pointer: an array of row_pointer indices.  Each index stores the number of non-zero elements up to but not including the ith row.  
	Returns:
		A: The reconstructed matrix
	'''
    A = np.zeros((m, n))
    for row in range(n):
        rowptr = row_pointer[row]
        if rowptr is not None: 
            A[row, columns[row_pointer[row]:row_pointer[row+1]]] = values[row_pointer[row]:row_pointer[row+1]]
            print(A[row, :])
            time.sleep(2)
    return A 

csr_reconstruction(values, columns, row_pointer, 8, 8)

            
