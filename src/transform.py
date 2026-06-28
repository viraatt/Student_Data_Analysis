"""
Module 4 & 5: Data Transformation and Filtering
"""

import pandas as pd


def assign_grade(row):
    marks = row["Marks"]
    attendance = row["Attendance"]

    # If attendance is too low, drop the grade by one level
    low_attendance = attendance < 75

    if marks >= 90:
        return "B" if low_attendance else "A"
    elif marks >= 75:
        return "C" if low_attendance else "B"
    elif marks >= 60:
        return "D" if low_attendance else "C"
    elif marks >= 40:
        return "F" if low_attendance else "D"
    else:
        return "F"


def assign_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


def performance_score(row):
    return round((row["Marks"] * 0.6) + (row["Attendance"] * 0.25) + (row["StudyHours"] * 0.15), 2)


def transform_data(df):

    print("\nTASK #3 is the transform the given data and store it in different files accordingly")

    df["Grade"] = df.apply(assign_grade, axis=1)
    df["Result"] = df["Marks"].apply(assign_result)
    df["Performance Score"] = df.apply(performance_score, axis=1)

    print("\nSample after transformation:")
    print(df[["Name", "Marks", "Attendance", "Grade", "Result", "Performance Score"]].head(10))

    return df


def filter_data(df):

    print("\nDATA FILTERING AND STORAGE .......TASK->5")

    toppers = df[df["Grade"] == "A"]
    toppers.to_csv("output/toppers.csv", index=False)
    print(f"Toppers: {len(toppers)} students saved")

    failed = df[df["Result"] == "Fail"]
    failed.to_csv("output/failed_students.csv", index=False)
    print(f"Failed Students: {len(failed)} students saved")

    low_attendance = df[df["Attendance"] < 75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)
    print(f"Low Attendance {len(low_attendance)} students saved")


    high_study = df[df["StudyHours"] > 8]
    high_study.to_csv("output/high_study_hours.csv", index=False)
    print(f"High Study Hours: {len(high_study)} students saved")