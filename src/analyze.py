"""
Module 6-9: Analysis, Sorting, Grouping and Stats
"""

import pandas as pd


def analyze_data(df):

    print("\nTask 6 is to analyze the data and give meaningfull statistics ")

    print("\nAverage Marks:", round(df["Marks"].mean(), 2))
    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())
    print("Average Attendance:", round(df["Attendance"].mean(), 2))
    print("Average Study Hours:", round(df["StudyHours"].mean(), 2))

    # pass and fail percentage
    total = len(df)
    passed = len(df[df["Result"] == "Pass"])
    failed = len(df[df["Result"] == "Fail"])

    print("Pass Percentage", round(passed / total * 100, 2), "%")
    print("Fail Percentag:", round(failed / total * 100, 2), "%")

    print("\nGrade Distribution:")
    print(df["Grade"].value_counts())


def sort_data(df):

    print("\Task 7 is to sort the data and display by marks attendance and study hours ")

    print("\nSorted by Marks:")
    print(df.sort_values("Marks", ascending=False)[["Name", "Marks", "Grade"]].head(10))

    print("\nSorted by Attendance:")
    print(df.sort_values("Attendance", ascending=False)[["Name", "Attendance"]].head(10))

    print("\nSorted by Study Hours:")
    print(df.sort_values("StudyHours", ascending=False)[["Name", "StudyHours"]].head(10))


def group_data(df):

    print("\n==== MODULE 8: GROUPING ====")

    grouped = df.groupby("Grade").agg(
        Average_Marks=("Marks", "mean"),
        Total_Students=("Name", "count"),
        Average_Attendance=("Attendance", "mean")
    ).round(2)

    print(grouped)


def stats_analysis(df):

    print("\n==== MODULE 9: STATISTICAL ANALYSIS ====")

    cols = ["Marks", "Attendance", "StudyHours"]

    print("\nMean:\n", df[cols].mean().round(2))
    print("\nMedian:\n", df[cols].median().round(2))
    print("\nMode:\n", df[cols].mode().iloc[0].round(2))
    print("\nStd Deviation:\n", df[cols].std().round(2))
    print("\nVariance:\n", df[cols].var().round(2))

    # checking how marks and attendance relate to each other
    print("\nCorrelation (Marks vs Attendance):")
    print(df[["Marks", "Attendance"]].corr().round(3))

    print("\nCorrelation between marks and Study hours")
    print(df[["Marks","StudyHours"]].corr().round())