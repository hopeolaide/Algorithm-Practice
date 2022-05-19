'''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
'''

def reshape_matrix(matrix, r, c):
    row_num = len(matrix)
    column_num = len(matrix[0])

    if row_num*column_num != r*c:
        return matrix

    new_matrix = []
    for i in range(r):
        new_row = []
        for j in range(i*column_num, (i+1)*column_num):
            new_row+=matrix[j]
        new_matrix.append(new_row)
        
    return new_matrix 


# 2nd approach (incomplete):
""" 
My pseudocode:
Consider the length of the input_matrix and the length of each list in the input matrix. 
Implement a guard clause:
--Consider the possibility of reshaping the matrix with the given arguments. 
If not possible return the input_matrix.

--For each internal list in the matrix (array of arrays):
--consider the length of each internal list 
--append the index values of each element in the length of the internal list to an empty list.  

--Populate the new matrix with slices (or another method) of the new list based on the column number. 
Each list generated from slicing is a row in the new matrix.
"""

def reshape_matrix(input_matrix, row_num, column_num): 
# Consider the length of the input_matrix and the length of each list in the input matrix. 
    list_len = len(input_matrix[0])
    mat_len = len(input_matrix)
    flat_matrix = []
    new_row_list = []
    new_matrix = []
# Begin with a guard clause:
# --Consider the possibility of reshaping the matrix with the given arguments. If not possible return the input_matrix.
    if list_len*mat_len != row_num*column_num:
    # if row_num > len(flat_matrix):
        return input_matrix
        
    else:   
# For each internal list in the matrix (array of arrays):
        for list in input_matrix:
# --consider the length of each internal list 
            for index in range(len(list)+1):
# --append the index values of each element in the length of the internal list to an empty list.  
                flat_matrix.append(list[index])
                
        return flat_matrix
    
        while len(flat_matrix) > 0: 
            
# --Populate new matrix with slices of the new list based on the column number. Each list generated from slicing is a row in the new matrix.
    
    # new_row_list.append(flat_matrix[0:column_num+1])
            pass