"""
Bonus: Visualizations using Matplotlib
"""

import matplotlib.pyplot as plt
import os

os.makedirs("output/charts", exist_ok=True)


def plot_grade_bar(df):

    grade_counts = df["Grade"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar(grade_counts.index, grade_counts.values, color=["green", "blue", "orange", "red", "black"])
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.savefig("output/charts/grade_bar.png")
    plt.show()
    print("Saved: grade_bar.png")


def plot_grade_pie(df):

    grade_counts = df["Grade"].value_counts().sort_index()

    plt.figure(figsize=(6, 6))
    plt.pie(grade_counts.values, labels=grade_counts.index, autopct="%1.1f%%")
    plt.title("Grade Distribution")
    plt.savefig("output/charts/grade_pie.png")
    plt.show()
    print("Saved: grade_pie.png")


def plot_scatter(df):

    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Marks"], alpha=0.5, color="purple")
    plt.title("Marks vs Attendance")
    plt.xlabel("Attendance")
    plt.ylabel("Marks")
    plt.savefig("output/charts/marks_vs_attendance.png")
    plt.show()
    print("Saved: marks_vs_attendance.png")


def run_visualizations(df):

    print("\n==== BONUS: VISUALIZATIONS ====")
    plot_grade_bar(df)
    plot_grade_pie(df)
    plot_scatter(df)