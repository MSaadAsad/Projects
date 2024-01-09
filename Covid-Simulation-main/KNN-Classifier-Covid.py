import statistics
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load CSV file into Pandas DataFrame."""
    return pd.read_csv(file_path)

def data_parser(data):
    """Converts data points to z-scores.

    Args:
        data: Pandas DataFrame containing the data set.

    Returns:
        A list containing infected status, temperature, WBC count, headache severity, and cough severity.
    """
    columns = ["Infected", "Temperature", "WBC Count", "Headache Severity", "Cough Severity"]
    for col in columns[1:]:
        mean = statistics.mean(data[col])
        stdev = statistics.stdev(data[col])
        data[col] = (data[col] - mean) / stdev

    return [list(data[col]) for col in columns]

def knn_classifier(learning_data, test_data, k):
    """Classifies the test data based on k-nearest neighbors.

    Args:
        learning_data: Parsed data set used for learning.
        test_data: Data to be classified.
        k: Number of nearest neighbors to consider.

    Prints:
        Diagnosis as "Infected" or "Normal".
    """
    difference = []
    for i in range(len(learning_data[0])):
        diff = sum((test_data[j+1] - learning_data[j+1][i]) ** 2 for j in range(4))
        difference.append(diff)

    sorted_difference = sorted(difference)
    count = sum(1 for i in range(k) if learning_data[0][difference.index(sorted_difference[i])] == 1)

    if count > k / 2:
        print("Infected")
    else:
        print("Normal")

file_path = "/Users/muhammadsaadasad/Downloads/CS51_Assignment_Diagnosis_Data.csv"
data = load_data(file_path)
output_list = data_parser(data)
