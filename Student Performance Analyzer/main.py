import pandas as pd

from functions_using import *
# Load the CSV file
df = pd.read_csv('data/students.csv')

print(""" 
      
=============================
 STUDENT PERFORMANCE REPORT
=============================

""")

df = calculate_total(df)
df = calculate_average(df)
df = calculate_result(df)
df = calculate_grade(df)
grade_counts = get_grade_counts(df)

top_students = get_top_students(df)

print("\nTop 5 Students:")
print(top_students)

plot_top_students(top_students)


