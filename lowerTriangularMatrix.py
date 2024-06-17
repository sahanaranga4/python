import numpy as np

# Define the matrices P, D, and P^-1
P = np.array([[1, 1, -1], [0, 1, 1], [0, 0, 1]])
print(P)
D = np.diag([2, 1, -1])  # Diagonal matrix with eigenvalues
P_inv = np.array([[1, 0, 0], [-1, 1, 0], [2, -1, 1]])

# Calculate A = PDP^-1
A = np.dot(np.dot(P,D), P_inv)
print(A)

# Convert the upper triangular part to zeros
A[np.triu_indices_from(A, k=1)] = 0


print("Lower triangular matrix A:")
print(A)
