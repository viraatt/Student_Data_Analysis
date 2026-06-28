# Student Performance Data Analysis System

A data analysis project built with Python and Pandas that processes
student records and generates meaningful insights.



## Module Breakdown

### load_data.py
Reads the CSV file and displays basic info like
first/last rows, shape, column names and data types.

### clean_data.py
- Inspects the data for missing values and duplicates
- Fills missing values with median
- Removes rows with invalid values

### transform.py
- Assigns Grade based on Marks + Attendance
- Assigns Pass/Fail Result
- Calculates a Performance Score
- Filters and saves student subsets

### analyze.py
- Calculates averages, highest, lowest marks
- Groups students by grade
- Computes statistics like mean, median, std

### report.py
- Generates a final summary report
- Saves everything to the output folder

---

## Grading Logic

| Marks | Attendance >= 75% | Attendance < 75% |
|-------|-------------------|------------------|
| >= 90 | A                 | B                |
| >= 75 | B                 | C                |
| >= 60 | C                 | D                |
| >= 40 | D                 | F                |
| < 40  | F                 | F                |

> Low attendance penalizes the grade by one level.

---

## Performance Score Formula
Marks carry the most weight, attendance second, study hours third.

---

## Output Filesls

| File | Description |
|------|-------------|
| cleaned_data.csv | Dataset after cleaning |
| toppers.csv | Students with Grade A |
| failed_students.csv | Students who failed |
| low_attendance.csv | Attendance below 75% |
| high_study_hours.csv | Study hours above 8 |
| report.csv | Final summary report |