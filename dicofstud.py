#Create a dictionary of student names and their scores, then find the average score
student_scores = {'Juned': 85,'Samarth': 92,'Onkar': 78,'Atipra': 95,'Zeeshan': 88}
average_score = sum(student_scores.values()) / len(student_scores)
print("Student Scores: ")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\nAverage Score:", average_score)
