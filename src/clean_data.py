#this is to clean the data find missing values and finally fill them using the median value 
import pandas as pd


def inspect_data(df):

    

    
    print("\nMissing Values")
    print(df.isnull().sum())

    
    print("\nDuplicate Record")
    print(df.duplicated().sum())
    

    
    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))

    print("\nDataset Info:")
    df.info()


def clean_data(df):

    print("\nTASK 2 ---> clean the data ")

   
    df = df.drop_duplicates()
    print("Duplicates removed")

   
    for col in ["StudyHours", "Attendance", "Marks"]:
        df[col] = df[col].fillna(df[col].median())
    print("Missing values filled")

   
    df = df[df["StudyHours"].between(0, 24)]
    df = df[df["Attendance"].between(0, 100)]
    df = df[df["Marks"].between(0, 100)]
    print("Invalid entries removed")

    df.reset_index(drop=True, inplace=True)

    
    df.to_csv("output/cleaned_data.csv", index=False)
    print("Saved: cleaned_data.csv")

    return df
