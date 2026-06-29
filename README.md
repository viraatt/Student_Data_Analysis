# Student Performance Data Analysis System

A data analysis project built with Python and Pandas that processes
student records and generates meaningful insights.

---


## How to Run

    pip install pandas matplotlib
    python main.py

    or

    
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