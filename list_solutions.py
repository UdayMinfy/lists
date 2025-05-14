### Easy Questions

### 1. **List Operations** 

def filter_even_numbers(numbers):
    numbers=[i for i in numbers if i%2==0]
    return numbers
l=[2,3,4,1,5,7]
print(filter_even_numbers(l))


### 2. List Manipulation

def merge_sorted_lists(list1,list2):
    list1.extend(list2)
    return list1.sort()
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  


# Medium Questions

### 1. List Comprehensions
def generate_matrix(n,m):
    matrix=[i*j for i in range(n) for j in range(m)]
    return matrix 
print(generate_matrix(3,3))


### 2. Nested Lists 
def transpose_matrix(matx):
    rows = len(matx)
    cols = len(matx[0])
    
    # Initialize an empty matrix with dimensions cols x rows
    transposed_matx = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matx[j][i] = matx[i][j]

    return transposed_matx
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))




