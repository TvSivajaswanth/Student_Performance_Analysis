import numpy as np
def calculate_total(df):
    subject_columns = ["Python", "Maths", "English", "Science"]

    df["Total"] = df[subject_columns].sum(axis=1)

    return df


def calculate_average(df):
    df["Average"] = df["Total"] / 4

    return df


def calculate_result(df):
    df["Result"] = df["Average"].apply(
        lambda x: "Pass" if x >= 70 else "Fail"
    )

    return df


def grade_system(average):

    if average > 90:
        return "A"

    elif average > 85:
        return "B"

    elif average > 70:
        return "C"

    elif average > 60:
        return "D"

    else:
        return "F"
    
def calculate_grade(df):
    df["Grade"] = df["Average"].apply(grade_system)

    return df


def height_avarage_student(df):
    
    height_avarage_students = df.loc[df['Average'] == df['Average'].max(),["Name","Average"]]

    print(height_avarage_students.to_string(index=False))
    
    
def get_subject_averages(df):
    subject_columns = ["Python", "Maths", "English", "Science"]
    return df[subject_columns].mean()


def get_top_student(df):
   
    top_student = df.loc[df["Average"] == df['Average'].max(),["Name","Average"]]
    
    return top_student.to_string(index = False)

def get_students_needing_improvement(df):
   
    
    needing_improvement = df.loc[df["Average"] < 70,["Name", "Average"]]
    
    return needing_improvement.to_string(index = False)
    
def get_grade_counts(df):
       
    count = df["Grade"].value_counts().sort_index()
    
    return count

def get_numpy_statistics(df):
    python_marks = np.array(df["Python"])

    average = np.mean(python_marks)
    maximum = np.max(python_marks)
    minimum = np.min(python_marks)
    total = np.sum(python_marks)
     
    print(f""" 
      
Python Average: {average}
Python Highest: {maximum}
Python Lowest: {minimum}
Python Total: {total}
      """)

def get_top_students(df, n=5):
    return df.nlargest(n, "Average")[["Name", "Average"]]