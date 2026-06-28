#This module is being used for data loading and has function to display the basic details
import pandas as pd


def load_data():
    df = pd.read_csv("data\student_dataset_v2.csv")
    print("Dataset loaded successfully!")
    return df


def display_basic_info(df):

    print("\n TASK 1 -> load the data and show basic details ")

    # First 5 rows
    print("\nFirst 5 Records:")
    print(df.head())

    # Last 5 rows
    print("\nLast 5 Records:")
    print(df.tail())

    # Shape
    print("\nShape of Dataset:")
    print(df.shape)

    # Column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Data types
    print("\nData Types:")
    print(df.dtypes)
 