"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
column are set to 0.
"""
def  print_mat(mat):
    str_mat = ""
    for  row in mat:
        for item in row:
            str_mat += str(item) + (" "*(3- len(str(item))) )
        
        str_mat += "\n"
    
    print(str_mat)

def nullfy_row(mat,row):
    for i in range(0,len(mat[0])):
        mat[row][i] = 0

def nullfy_col(mat,col):
    for i in range(0,len(mat)):
        mat[i][col] = 0


def zero_matrix(mat):
    print_mat(mat)
    rowHaszero = False
    colHaszero = False

    for i in range(0,len(mat[0])):
        if mat[0][i] == 0:
            rowHaszero = True
            break

    for i in range(0,len(mat)):
        if mat[i][0] == 0:
            colHaszero = True
            break


    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    
    for i in range(0,len(mat)):
        if mat[i][0] == 0:
            nullfy_row(mat,i)

    for j in range(0,len(mat[0])):
        if mat[0][j] == 0:
            nullfy_col(mat,j)

    if rowHaszero:
        nullfy_row(mat,0)


    if colHaszero:
        nullfy_col(mat,0)

    return mat


print_mat(zero_matrix([[1,2,3,4],[5,6,0,7],[8,0,9,10],[11,12,13,14]]))



