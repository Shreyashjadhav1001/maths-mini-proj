from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def parse_matrix(matrix_str):
    """Convert user input into a NumPy array safely"""
    try:
        matrix = np.array([[float(num) for num in row.split()] for row in matrix_str.strip().split('\n')])
        return matrix
    except ValueError:
        return None  # Handle invalid inputs gracefully

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            matrix1 = parse_matrix(request.form['matrix1'])

            if matrix1 is None:
                raise ValueError("Invalid matrix input. Please enter numbers only, separated by spaces.")

            if operation in ['add', 'subtract', 'multiply']:
                matrix2 = parse_matrix(request.form['matrix2'])
                if matrix2 is None:
                    raise ValueError("Invalid second matrix input.")

            # Perform operations
            if operation == 'add':
                result = np.round(matrix1 + matrix2, 2).tolist()
            elif operation == 'subtract':
                result = np.round(matrix1 - matrix2, 2).tolist()
            elif operation == 'multiply':
                if matrix1.shape[1] != matrix2.shape[0]:
                    raise ValueError("Number of columns in Matrix 1 must equal number of rows in Matrix 2.")
                result = np.round(np.dot(matrix1, matrix2), 2).tolist()
            elif operation == 'determinant':
                if matrix1.shape[0] != matrix1.shape[1]:
                    raise ValueError("Determinant is only for square matrices.")
                result = round(float(np.linalg.det(matrix1)), 2)
            elif operation == 'inverse':
                if matrix1.shape[0] != matrix1.shape[1]:
                    raise ValueError("Inverse is only for square matrices.")
                if np.linalg.det(matrix1) == 0:
                    raise ValueError("Matrix is singular and does not have an inverse.")
                result = np.round(np.linalg.inv(matrix1), 2).tolist()
            elif operation == 'eigen':
                if matrix1.shape[0] != matrix1.shape[1]:
                    raise ValueError("Eigenvalues and eigenvectors require a square matrix.")
                eigenvalues, eigenvectors = np.linalg.eig(matrix1)
                result = {
                    "Eigenvalues": [round(float(ev), 2) for ev in eigenvalues],
                    "Eigenvectors": np.round(eigenvectors, 2).tolist()
                }

        except Exception as e:
            error = str(e)



    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
