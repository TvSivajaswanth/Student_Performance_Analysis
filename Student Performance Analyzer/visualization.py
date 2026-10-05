import matplotlib.pyplot as plt


def plot_subject_averages(subject_averages):
    subjects = subject_averages.index
    averages = subject_averages.values

    plt.bar(subjects, averages)

    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Average Marks by Subject")

    plt.show()
    
def plot_grade_distribution(grade_counts):
    grades = grade_counts.index
    counts = grade_counts.values

    plt.bar(grades, counts)

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Grade Distribution")

    plt.show()   
    
    
def plot_top_students(top_students):
    names = top_students["Name"]
    averages = top_students["Average"]

    plt.bar(names, averages)

    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Top 5 Students")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()     