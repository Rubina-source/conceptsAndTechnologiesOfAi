# -*- coding: utf-8 -*-
"""worksheet5_Rubina.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KngJcBvHBLSRaa6Vo_N463_QsmY6pL6j
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/AI/student.csv")
df

from google.colab import drive
drive.mount('/content/drive')

df.head(5)

df.tail(5)

df.info()

df.describe()

import pandas as pd
# Splitting the data into Features (X) and Labels (Y)
X = df.iloc[:, :-1]  # Assuming all columns except the last are features
Y = df.iloc[:, -1]   # Assuming the last column is the label
X.head()

Y.head()

X_matrix = X.T.to_numpy()
Y_matrix = Y.to_numpy().reshape(-1, 1)

W = np.random.rand(X_matrix.shape[0], 1)

Y_hat = np.dot(W.T, X_matrix)

print("Shape of Feature Matrix (X):", X_matrix.shape)
print("Shape of Weight Vector (W):", W.shape)
print("Shape of Target Vector (Y):", Y_matrix.shape)
print("Shape of Predicted Y (Y_hat):", Y_hat.shape)

print("\nSample Feature Matrix (X):")
print(X_matrix[:, :5])

print("\nSample Weight Vector (W):")
print(W)

print("\nSample Target Vector (Y):")
print(Y_matrix[:5])

print("\nSample Predicted Y (Y_hat):")
print(Y_hat[:, :5])

# Step 1: Split the dataset into training and testing sets (80-20 split)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42) # Transpose X back to (1000, 2)

# Check the dimensions of the split data
print("Training Data (X_train) Shape:", X_train.shape)
print("Testing Data (X_test) Shape:", X_test.shape)
print("Training Labels (Y_train) Shape:", Y_train.shape)
print("Testing Labels (Y_test) Shape:", Y_test.shape)

# Optionally, if you want to confirm the split visually:
# Print the first few entries of X_train and Y_train
print("\nFirst few entries of X_train:\n", X_train[:5])
print("\nFirst few entries of Y_train:\n", Y_train[:5])

def cost_function(X, Y, W):
    """
    Parameters:
    X : numpy.ndarray
        Feature matrix (d x n), where d is the number of features and n is the number of samples.
    Y : numpy.ndarray
        Target vector (n, ), where n is the number of samples.
    W : numpy.ndarray
        Weight vector (d, ), where d is the number of features.

    Output:
    cost : float
        The accumulated mean squared error (MSE).
    """
    # Step 1: Calculate the predicted values (Y_hat) using the linear model
    Y_pred = np.dot(X, W)  # X * W gives the predicted values

    # Step 2: Calculate the squared errors between the predicted and actual values
    errors = Y - Y_pred

    # Step 3: Compute the Mean Squared Error (MSE)
    cost = np.mean(errors ** 2)  # MSE = average of squared errors

    return cost

# Define the cost function
def cost_function(X, Y, W):
    """
    Parameters:
    X : numpy.ndarray
        Feature matrix (d x n), where d is the number of features and n is the number of samples.
    Y : numpy.ndarray
        Target vector (n, ), where n is the number of samples.
    W : numpy.ndarray
        Weight vector (d, ), where d is the number of features.

    Output:
    cost : float
        The accumulated mean squared error (MSE).
    """
    # Step 1: Calculate the predicted values (Y_hat) using the linear model
    Y_pred = np.dot(X, W)  # X * W gives the predicted values

    # Step 2: Calculate the squared errors between the predicted and actual values
    errors = Y - Y_pred

    # Step 3: Compute the Mean Squared Error (MSE)
    cost = np.mean(errors ** 2)  # MSE = average of squared errors

    return cost

# Test case
X_test = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
Y_test = np.array([3, 7, 11])
W_test = np.array([1, 1])

# Calculate the cost
cost = cost_function(X_test, Y_test, W_test)

# Check if the cost is as expected (0)
if cost == 0:
    print("Proceed Further")
else:
    print("Something went wrong: Reimplement the cost function")

print("Cost function output:", cost)

# Define the cost function
def cost_function(X, Y, W):
    """
    Parameters:
    X : numpy.ndarray
        Feature matrix (m x n), where m is the number of samples and n is the number of features.
    Y : numpy.ndarray
        Target vector (m, ), where m is the number of samples.
    W : numpy.ndarray
        Weight vector (n, ), where n is the number of features.

    Output:
    cost : float
        The accumulated mean squared error (MSE).
    """
    # Calculate the predicted values
    Y_pred = np.dot(X, W)

    # Calculate the squared errors
    errors = Y - Y_pred

    # Compute the Mean Squared Error (MSE)
    cost = np.mean(errors ** 2)

    return cost

# Define the gradient descent function
def gradient_descent(X, Y, W, alpha, iterations):
    """
    Perform gradient descent to optimize the parameters of a linear regression model.

    Parameters:
    X : numpy.ndarray
        Feature matrix (m x n).
    Y : numpy.ndarray
        Target vector (m x 1).
    W : numpy.ndarray
        Initial guess for parameters (n x 1).
    alpha : float
        Learning rate.
    iterations : int
        Number of iterations for gradient descent.

    Returns:
    W_update : numpy.ndarray
        Updated parameters (n x 1).
    cost_history : list
        History of cost values over iterations.
    """
    # Initialize cost history
    cost_history = []

    # Number of samples (m)
    m = len(Y)

    # Gradient descent loop
    for iteration in range(iterations):
        # Step 1: Hypothesis Values (hθ(X) = X * W)
        Y_pred = np.dot(X, W)

        # Step 2: Loss (Difference between predicted and actual values)
        loss = Y_pred - Y

        # Step 3: Gradient Calculation (dw = (2/m) * X^T * loss)
        dw = (2/m) * np.dot(X.T, loss)

        # Step 4: Update weights (W = W - alpha * dw)
        W_update = W - alpha * dw

        # Step 5: Calculate the new cost value and store it in cost_history
        cost = cost_function(X, Y, W_update)
        cost_history.append(cost)

        # Update weights for the next iteration
        W = W_update

    return W_update, cost_history

# Example Usage:

# Sample dataset (Feature matrix X and target vector Y)
X = np.array([[1, 3, 5],
              [2, 4, 6],
              [1, 3, 5],
              [2, 4, 6]])  # (4 samples, 3 features)

Y = np.array([3, 7, 3, 7])  # Target values (4 samples)

# Initialize weights (W) randomly or set to zeros
W_init = np.zeros(X.shape[1])  # (3 features)

# Set learning rate and number of iterations
alpha = 0.01
iterations = 1000

# Call gradient descent
W_optimal, cost_history = gradient_descent(X, Y, W_init, alpha, iterations)

# Print results
print("Optimized Weights:", W_optimal)
print("Final Cost:", cost_history[-1])
print("Cost History (first 10 iterations):", cost_history[:10])

# Generate random test data
np.random.seed(0) # For reproducibility
X = np.random.rand(100, 3) # 100 samples, 3 features
Y = np.random.rand(100)
W = np.random.rand(3) # Initial guess for parameters
# Set hyperparameters
alpha = 0.01
iterations = 1000
# Test the gradient_descent function
final_params, cost_history = gradient_descent(X, Y, W, alpha, iterations)
# Print the final parameters and cost history
print("Final Parameters:", final_params)
print("Cost History:", cost_history)

# Model Evaluation - RMSE
def rmse(Y, Y_pred):
    """
    This function calculates the Root Mean Squared Error (RMSE).

    Parameters:
    Y : numpy.ndarray
        Array of actual (target) dependent variables (m, ).
    Y_pred : numpy.ndarray
        Array of predicted dependent variables (m, ).

    Returns:
    rmse : float
        The root mean squared error.
    """
    # Step 1: Calculate the squared differences between actual and predicted values
    squared_differences = (Y - Y_pred) ** 2

    # Step 2: Calculate the mean of the squared differences
    mean_squared_error = np.mean(squared_differences)

    # Step 3: Take the square root of the mean squared error
    rmse_value = np.sqrt(mean_squared_error)

    return rmse_value

# Model Evaluation - R-squared
def r2(Y, Y_pred):
    """
    This function calculates the R Squared value, which measures the goodness of fit.

    Parameters:
    Y : numpy.ndarray
        Array of actual (target) dependent variables (m, ).
    Y_pred : numpy.ndarray
        Array of predicted dependent variables (m, ).

    Returns:
    r2 : float
        The R-squared value.
    """
    # Step 1: Calculate the mean of the actual values (Y)
    mean_y = np.mean(Y)

    # Step 2: Calculate the Total Sum of Squares (SST)
    ss_tot = np.sum((Y - mean_y) ** 2)

    # Step 3: Calculate the Sum of Squared Residuals (SSR)
    ss_res = np.sum((Y - Y_pred) ** 2)

    # Step 4: Calculate the R-squared value
    r2_value = 1 - (ss_res / ss_tot)

    return r2_value

# Gradient Descent Function (as you wrote earlier)
def gradient_descent(X, Y, W, alpha, iterations):
    cost_history = [0] * iterations
    m = len(Y)

    for iteration in range(iterations):
        # Step 1: Hypothesis Values
        Y_pred = np.dot(X, W)  # Predicted Y values
        # Step 2: Difference between Hypothesis and Actual Y
        loss = Y_pred - Y
        # Step 3: Gradient Calculation
        dw = (1/m) * np.dot(X.T, loss)  # Gradient for the weights
        # Step 4: Updating Values of W using Gradient
        W -= alpha * dw
        # Step 5: New Cost Value
        cost = cost_function(X, Y, W)
        cost_history[iteration] = cost

    return W, cost_history

# Cost Function
def cost_function(X, Y, W):
    m = len(Y)
    Y_pred = np.dot(X, W)
    cost = (1 / (2 * m)) * np.sum(np.square(Y_pred - Y))
    return cost

# Model Evaluation - RMSE
def rmse(Y, Y_pred):
    return np.sqrt(np.mean((Y - Y_pred) ** 2))

# Model Evaluation - R2
def r2(Y, Y_pred):
    ss_tot = np.sum((Y - np.mean(Y)) ** 2)
    ss_res = np.sum((Y - Y_pred) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2
def main():
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Step 1: Load the dataset
    data = pd.read_csv("C:\\Users\\user\\Desktop\\student.csv")

    # Step 2: Split the data into features (X) and target (Y)
    X = data[['Math', 'Reading']].values  # Features: Math and Reading marks
    Y = data['Writing'].values.reshape(-1, 1)  # Target: Writing marks as a column vector

    # Step 3: Split the data into training and test sets (80% train, 20% test)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Step 4: Initialize weights (W) to zeros, learning rate, and number of iterations
    W = np.zeros((X_train.shape[1], 1))  # Initialize weights as a column vector
    alpha = 0.00001  # Learning rate
    iterations = 1000  # Number of iterations for gradient descent

    # Step 5: Perform Gradient Descent
    W_optimal, cost_history = gradient_descent(X_train, Y_train, W, alpha, iterations)

    # Step 6: Make predictions on the test set
    Y_pred = np.dot(X_test, W_optimal)

    # Step 7: Evaluate the model using RMSE and R-Squared
    model_rmse = rmse(Y_test, Y_pred)
    model_r2 = r2(Y_test, Y_pred)

    # Step 8: Output the results
    print("Final Weights:", W_optimal.flatten())
    print("Cost History (First 10 iterations):", cost_history[:10])
    print("RMSE on Test Set:", model_rmse)
    print("R-Squared on Test Set:", model_r2)

# Execute the main function
if __name__ == "__main__":
    main()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to calculate Cost (Mean Squared Error)
def cost_function(X, Y, W):
    m = len(Y)
    Y_pred = np.dot(X, W)
    cost = (1/(2*m)) * np.sum((Y_pred - Y) ** 2)
    return cost

# Gradient Descent function
def gradient_descent(X, Y, W, alpha, iterations):
    cost_history = []
    m = len(Y)
    for _ in range(iterations):
        Y_pred = np.dot(X, W)
        loss = Y_pred - Y
        dw = (1/m) * np.dot(X.T, loss)
        W = W - alpha * dw
        cost = cost_function(X, Y, W)
        cost_history.append(cost)
    return W, cost_history

# Root Mean Squared Error (RMSE)
def rmse(Y, Y_pred):
    return np.sqrt(np.mean((Y - Y_pred) ** 2))

# R-Squared function
def r2(Y, Y_pred):
    ss_tot = np.sum((Y - np.mean(Y)) ** 2)
    ss_res = np.sum((Y - Y_pred) ** 2)
    return 1 - (ss_res / ss_tot)

# Main Function to integrate all steps
def main():
    # Load the dataset
    data = pd.read_csv("C:\\Users\\user\\Desktop\\student.csv")  # Replace with your actual CSV file
    X = data[['Math', 'Reading']].values  # Features
    Y = data['Writing'].values  # Target

    # Split the dataset into training and test sets (80% train, 20% test)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Initialize weights, number of iterations, and learning rates
    W_initial = np.zeros(X_train.shape[1])
    iterations = 1000

    # Experiment with different learning rates
    learning_rates = [0.0001, 0.001, 0.01, 0.1, 0.5]

    for alpha in learning_rates:
        print(f"Experimenting with Learning Rate: {alpha}")

        # Train the model using Gradient Descent
        W_optimal, cost_history = gradient_descent(X_train, Y_train, W_initial, alpha, iterations)

        # Make predictions on the test set
        Y_pred = np.dot(X_test, W_optimal)

        # Evaluate the model
        model_rmse = rmse(Y_test, Y_pred)
        model_r2 = r2(Y_test, Y_pred)

        # Output the results
        print("Final Weights:", W_optimal)
        print("Final Cost (Last Iteration):", cost_history[-1])
        print("RMSE on Test Set:", model_rmse)
        print("R-Squared on Test Set:", model_r2)
        print("-" * 50)

# Execute the main function
if __name__ == "__main__":
    main()

