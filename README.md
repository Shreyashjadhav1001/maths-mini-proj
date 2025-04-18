
# Matrix Calculator Web Application

A web-based **Matrix Calculator** built using **Flask** and **NumPy**. 
This application allows users to perform various matrix operations like addition, subtraction, multiplication, determinant, inverse, and eigenvalue/eigenvector calculation.

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** (Web Framework)
- **NumPy** (Matrix Operations)
- **HTML/CSS** (Frontend Design)
- **Matplotlib** (for Eigenvector Visualization)

## 📦 Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Shreyashjadhav1001/maths-mini-proj.git
cd maths-mini-proj
```

### 2. Set up a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to isolate project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary libraries using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, you can install them manually:

```bash
pip install flask numpy matplotlib
```

## 🧑‍💻 How to Run the Flask Application

### 1. Run the Flask Application

After installing the dependencies, you can run the Flask app by executing:

```bash
python app.py
```

This will start the Flask development server.

### 2. Access the Application

Open your web browser and go to:

```
http://127.0.0.1:5000/
```

You will be directed to the Matrix Calculator web interface.

## 📁 Project Structure

```
maths-mini-proj/
│
├── app.py                # Main Flask application file
├── templates/            # HTML templates
│   └── index.html       # HTML template for the main user interface
├── requirements.txt      # List of Python dependencies
└── README.md             # Project documentation
```

## ⚙️ Features

- **Matrix Operations Available**:
  - **Addition**
  - **Subtraction**
  - **Multiplication**
  - **Determinant** (only for square matrices)
  - **Inverse** (only for square matrices)
  - **Eigenvalues and Eigenvectors** (only for square matrices)

- **Interactive Form**:
  - Input matrices directly through text areas.
  - Choose the desired operation from a dropdown menu.

- **Error Handling**:
  - Provides user-friendly error messages when invalid matrix inputs are provided.

- **Eigenvector Visualization**:
  - When calculating eigenvalues and eigenvectors, the eigenvectors are visualized using `matplotlib`.

## 📋 How to Use

1. **Matrix Input**:
   - **Matrix 1**: Enter the first matrix row-wise, with each row separated by a new line and numbers in each row separated by spaces.
   - **Matrix 2 (if needed)**: Enter the second matrix (required for addition, subtraction, and multiplication).
   
2. **Choose Operation**:
   - Select the operation you wish to perform (e.g., addition, subtraction, determinant).

3. **Submit**:
   - Click the **Calculate** button to perform the selected operation. The result will be displayed below the form.

### Example Input:

**Matrix 1:**
```
1 2
3 4
```

**Matrix 2:**
```
5 6
7 8
```

**Operation: Matrix Addition**

### Example Result:

```
Matrix Addition Result:
[[ 6.  8.]
 [10. 12.]]
```

### Error Handling:

If invalid input is provided (e.g., non-numeric characters in the matrix), the error message will be displayed:

```
Error:
Invalid matrix input. Please enter numbers only, separated by spaces.
```

## 🎨 Frontend Design

The frontend is designed with a clean, dark theme with a modern user interface. It includes:

- A central form to input matrices and choose operations.
- Clear and responsive result/error displays.
- Buttons and input fields are styled for ease of use.

### Styles Used:
- Background color: Dark theme with neon accents for buttons and highlights.
- Buttons: Hover effect to improve user interaction.
- Form elements: Styled for uniformity and clarity.

## 📝 Notes

- Ensure Python 3.x is installed on your system.
- The Flask app runs by default on port 5000. You can change this by modifying the `app.run()` method in `app.py`.
- For advanced operations like inverse or eigenvalue calculations, make sure your matrices are square.
  
### Eigenvalue/Eigenvector Visualization:
- When performing eigenvalue and eigenvector calculations, the eigenvectors will be displayed as arrows on a 2D plot using `matplotlib`.
