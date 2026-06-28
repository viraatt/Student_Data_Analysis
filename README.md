# Student Performance Data Analysis System

A data analysis project built with Python and Pandas that processes
student records and generates meaningful insights.

---

## Project Structure

    Student_Data_Analysis/
    ├── data/
    │   └── student_dataset_v2.csv   # Raw input data
    ├── output/
    │   ├── cleaned_data.csv         # After cleaning
    │   ├── toppers.csv              # Grade A students
    │   ├── failed_students.csv      # Students who failed
    │   ├── low_attendance.csv       # Attendance below 75%
    │   ├── high_study_hours.csv     # Study hours above 8
    │   ├── report.csv               # Final summary report
    │   └── charts/
    │       ├── grade_bar.png        # Grade bar chart
    │       ├── grade_pie.png        # Grade pie chart
    │       └── marks_vs_attendance  # Scatter plot
    ├── src/
    │   ├── load_data.py             # Module 1
    │   ├── clean_data.py            # Module 2 and 3
    │   ├── transform.py             # Module 4 and 5
    │   ├── analyze.py               # Module 6 to 9
    │   ├── report.py                # Module 10 and 11
    │   └── visualize.py             # Bonus: charts
    ├── main.py                      # Run this
    └── README.md                    # You are here

---

## How to Run

    pip install pandas matplotlib
    python main.py

---

## Module Breakdown

### load_data.py
Reads the CSV and shows first/last rows, shape and data types.

### clean_data.py
- Finds missing values and duplicates
- Fills missing values with median
- Removes rows with invalid values

### transform.py
- Assigns Grade based on Marks and Attendance
- Assigns Pass or Fail
- Calculates Performance Score
- Filters and saves student subsets

### analyze.py
- Averages, highest and lowest marks
- Groupby grade
- Mean, median, mode, std, variance
- Correlation between Marks and Attendance

### report.py
- Builds a summary with pass/fail counts and grade distribution
- Shows top 10 students by Performance Score
- Saves report.csv

### visualize.py (Bonus)
- Bar chart of grade distribution
- Pie chart of grade distribution
- Scatter plot of Marks vs Attendance

---

## Grading Logic

| Marks     | Attendance >= 75% | Attendance < 75% |
|-----------|-------------------|------------------|
| >= 90     | A                 | B                |
| >= 75     | B                 | C                |
| >= 60     | C                 | D                |
| >= 40     | D                 | F                |
| < 40      | F                 | F                |

Low attendance penalizes the grade by one level.

---

## Performance Score Formula

    Score = (Marks * 0.60) + (Attendance * 0.25) + (StudyHours * 0.15)

Marks carry the most weight, attendance second, study hours third.

---

## What I Learned

- How to load and explore a dataset using Pandas
- How to find and fix missing values and duplicates
- How to validate data and remove bad entries
- How to create new columns using apply and custom functions
- How to filter data into subsets and save them as CSV files
- How to group data and calculate aggregates using groupby
- How to compute basic statistics like mean, median, mode and correlation
- How to generate charts using Matplotlib
- How to organize a Python project into modules

---

## Correlation Finding

Checked correlation between Marks and Attendance in this dataset.
Result was nearly 0 because the data is randomly generated.
In a real dataset you would expect a moderate positive correlation
meaning students who attend more tend to score better.

---

## TBD

### Tkinter Desktop App
Plan to build a visual interface where users can:

- Upload any CSV file from their computer
- Automatically detect and map columns
- Run all analysis with one click
- View charts inside the app
- Download all output files in one go

This will make the project usable by anyone without
needing to touch the code or terminal at all.