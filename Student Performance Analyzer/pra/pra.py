import pandas as pd
import numpy as np
df = pd.read_csv('data/students.csv')

# print("Number of students: ?:",len(df))

# average_python_marks = df['Python'].mean()
# average_Maths_marks = df['Maths'].mean()
# average_English_marks = df['English'].mean()
# average_Science_marks = df['Science'].mean()

# print(f"Avarage of python?:{average_python_marks}")
# print(f"Avarage of Marhs?:{average_Maths_marks}")
# print(f"Avarage of English?:{average_English_marks}")
# print(f"Avarage of Science?:{average_Science_marks}\n")

# highest_Python_mark = df.loc[
#     df['Python'] == df['Python'].max(), 
#     "Name"
#     ].tolist()

# highest_Maths_mark = df.loc[
#     df['Maths'] == df['Maths'].max(), 
#     "Name"
#     ].tolist()

# print(f"Highest Python student: ?\n{highest_Python_mark}")

# print(f"Highest Maths student: ?\n{highest_Maths_mark}\n")


# # Finds rows where Python > 80, but ONLY returns the 'Names' column
# python_above_80 = df.loc[df['Python'] > 80, 'Name']

# Maths_below_70 = df.loc[df['Maths'] < 70, 'Name']

# print(f"Students with Python > 80 ?:\n{python_above_80.tolist()}\n")

# print(f"Students with maths < 70 ?:\n{Maths_below_70.tolist()}\n")



# df['Total'] = df[['Python', 'Maths', 'Science', 'English']].sum(axis=1)

# df["Average"] = df['Total'] / 4

# print(df[['Name','Total','Average']])
# print()

# height_avarage_student = df.loc[df['Average'] == df['Average'].max(),["Name","Average"]]

# print(f"Height Average of a Student is:\n{height_avarage_student.to_string(index=False)}\n")



# df['Result'] = df['Average'].apply(
    
#     lambda x: 'Pass' if x >= 70 else 'Fail'
    
#     )

# print(df[['Name', 'Average', 'Result']].to_string(index=False))
# print()

# all_pass_students = df.loc[df['Result'] == 'Pass',"Name"]

# print(f"All pass Students are: {len(all_pass_students)}\n")

# all_fail_students = df.loc[df['Result'] == 'Fail',["Name","Average"]]

# print(f"All fail Students are: {len(all_fail_students)}\n")

# print(f"Failed students are: \n{all_fail_students.to_string(index=False)}\n")




# def grade_system(avarage):
    
#     if avarage > 90:
        
#         return "A"
    
#     elif avarage > 85:
        
#         return "B"
    
#     elif avarage > 70:
        
#         return "C"
    
#     elif avarage > 60:
        
#         return "D"
    
#     else:
        
#         return "F"
    
    
# df["Grade"] = df['Average'].apply(grade_system)

# A_grade_count = df.loc[df['Grade'] == "A"] 
# B_grade_count = df.loc[df['Grade'] == "B"] 
# C_grade_count = df.loc[df['Grade'] == "C"] 
# D_grade_count = df.loc[df['Grade'] == "D"]
# F_grade_count = df.loc[df['Grade'] == "F"]
# """
# print(df['Grade'].value_counts().sort_index())

# """

# print("Grade A: ?",len(A_grade_count))
# print("Grade B: ?",len(B_grade_count))
# print("Grade C: ?",len(C_grade_count))
# print("Grade D: ?",len(D_grade_count))
# print("Grade F: ?",len(F_grade_count))






python_marks = np.array(df['Python'])


print(python_marks)
print(type(python_marks))

















