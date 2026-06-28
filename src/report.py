"""
Module 10 & 11: Report Generation and Export
"""

import pandas as pd


def generate_report(df):

    print("\n==== MODULE 10: REPORT GENERATION ====")

    total = len(df)
    passed = len(df[df["Result"] == "Pass"])
    failed = len(df[df["Result"] == "Fail"])

    # basic summary
    summary = {
        "Total Students": total,
        "Passed": passed,
        "Failed": failed,
        "Highest Marks": df["Marks"].max(),
        "Lowest Marks": df["Marks"].min(),
        "Average Marks": round(df["Marks"].mean(), 2),
        "Average Attendance": round(df["Attendance"].mean(), 2),
    }

    for key, val in summary.items():
        print(f"{key}: {val}")

    # grade wise breakdown
    print("\nGrade wise Distribution:")
    grade_dist = df["Grade"].value_counts().sort_index()
    print(grade_dist)

    # top 10 students by performance score
    print("\nTop 10 Students:")
    top10 = df.sort_values("Performance Score", ascending=False).head(10)
    print(top10[["Name", "Marks", "Attendance", "Grade", "Performance Score"]])

    # save report
    summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
    summary_df.to_csv("output/report.csv", index=False)
    print("\nSaved: report.csv")