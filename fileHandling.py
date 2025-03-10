import numpy as np

with open("loans.csv", "r") as file:
    content = file.read()


# Load data again, handling missing values
data = np.genfromtxt("loans.csv", delimiter=",", skip_header=1, usecols=8)

# Remove missing values
loan_amounts = data[~np.isnan(data)]

# Compute basic statistics
mean_loan = np.mean(loan_amounts)
print(mean_loan)

# Calculate median
meadian_loan = np.median(loan_amounts)
print(meadian_loan)

# Calculate Standard Deviation
std_loan = np.std(loan_amounts)
print(std_loan)