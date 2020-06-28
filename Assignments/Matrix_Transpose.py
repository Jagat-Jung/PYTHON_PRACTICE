matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]

inverse_matrix=[ ] 
matrix_liv=[]
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        temp=[matrix[j][i]]
        inverse_matrix=inverse_matrix+temp
    matrix_liv=matrix_liv+[inverse_matrix]
    inverse_matrix=[]
    
    
print(matrix_liv)


