"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
"""

def  print_mat(mat):
    str_mat = ""
    for  row in mat:
        for item in row:
            str_mat += str(item) + (" "*(3- len(str(item))) )
        
        str_mat += "\n"
    
    print(str_mat)

def rotate_matrix(mat):
    print_mat(mat)
    if  not len(mat) and len(mat) != len(mat[0]):
        return None

    mat_size = len(mat)

    for layer in range(0,mat_size//2):
        first = layer
        last = mat_size -1 - layer

        for i in range(first,last):
            offset = i - first

            # save top
            top = mat[first][i]

            #left -> top
            mat[first][i] = mat[last-offset][first]

            #bottom -> left
            mat[last-offset][first] = mat[last][last-offset]

            #right-> bottom
            mat[last][last-offset] = mat[i][last]

            #top -> right
            mat[i][last] = top

    return mat




print_mat(rotate_matrix([[1,2,3,4],[8,7,5,6],[9,10,11,12],[16,15,14,13]]))