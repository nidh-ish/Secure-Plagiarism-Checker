import random

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

def main():
    rows = random.randint(2, 5)
    cols = random.randint(2, 5)
    print(f"Generating a {rows}x{cols} matrix:")
    matrix = generate_matrix(rows, cols)
    print_matrix(matrix)
    
    print("\nTransposing the matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)

if __name__ == "__main__":
    main()
