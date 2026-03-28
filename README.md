ml-foundations

A beginner-friendly repository containing simple, from-scratch implementations of foundational machine learning algorithms in Python.

📘 Overview

This repository is designed to help learners understand the mathematical intuition and coding logic behind core machine learning techniques without relying on heavy frameworks. Each algorithm is implemented in a clear and transparent way, making it easy to follow and experiment with.

🔎 Algorithms Included

Gradient Descent (GD)

Linear Regression (LR)

Multiple Linear Regression (MLR)

🎯 Purpose

The goal of ml-foundations is to serve as a learning playground for students, hobbyists, and anyone curious about how machine learning works under the hood. By keeping the code simple and well-documented, the repo emphasizes conceptual clarity over production-ready complexity.

🚀 Getting Started

Clone the repository:

git clone https://github.com/sumantkumar0305/ml-foundations/.git

Navigate into the project folder:

cd ml-foundations

Run the Python scripts directly:

python gradient_descent.py

📂 Project Structure

ml-foundations/
│
├── gradient_descent.py
├── linear_regression.py
├── multiple_linear_regression.py
└── README.md

🧑‍💻 Requirements

Python 3.x

NumPy

Matplotlib (optional, for visualization)

Install dependencies:

pip install numpy matplotlib

📊 Example Usage

from linear_regression import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 5, 4, 5]

model = LinearRegression()
model.fit(X, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

🤝 Contributing

Contributions are welcome! If you’d like to add new algorithms, improve documentation, or fix bugs:

Fork the repo

Create a new branch (feature-new-algo)

Commit your changes

Open a pull request
