import numpy as np
import matplotlib.pyplot as plt

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the matrix row-wise:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    print("Choose an operation:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Determinant\n5. Inverse\n6. Eigenvalues and Eigenvectors")
    choice = int(input("Enter choice (1-6): "))
    
    if choice in [1, 2, 3]:
        print("Enter first matrix:")
        A = input_matrix()
        print("Enter second matrix:")
        B = input_matrix()
        
        if choice == 1:
            print("Matrix Addition Result:\n", A + B)
        elif choice == 2:
            print("Matrix Subtraction Result:\n", A - B)
        elif choice == 3:
            print("Matrix Multiplication Result:\n", np.dot(A, B))
    
    elif choice == 4:
        print("Enter matrix:")
        A = input_matrix()
        if A.shape[0] == A.shape[1]:
            print("Determinant:", np.linalg.det(A))
        else:
            print("Determinant is only for square matrices.")
    
    elif choice == 5:
        print("Enter matrix:")
        A = input_matrix()
        if A.shape[0] == A.shape[1]:
            try:
                print("Inverse:\n", np.linalg.inv(A))
            except np.linalg.LinAlgError:
                print("Matrix is singular, no inverse exists.")
        else:
            print("Inverse is only for square matrices.")
    
    elif choice == 6:
        print("Enter matrix:")
        A = input_matrix()
        if A.shape[0] == A.shape[1]:
            eigenvalues, eigenvectors = np.linalg.eig(A)
            print("Eigenvalues:", eigenvalues)
            print("Eigenvectors:\n", eigenvectors)
            
            # Visualizing eigenvectors
            plt.quiver([0, 0], [0, 0], eigenvectors[0, :], eigenvectors[1, :], angles='xy', scale_units='xy', scale=1, color=['r', 'b'])
            plt.xlim(-2, 2)
            plt.ylim(-2, 2)
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid()
            plt.show()
        else:
            print("Eigenvalues are only for square matrices.")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    matrix_operations()