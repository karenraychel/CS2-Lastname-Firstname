# Student Grade Calculator
name = input("Enter student name: ")
score1 = float(input("Enter Activity 1 score: "))
score2 = float(input("Enter Activity 2 score: "))
average = (score1 + score2) / 2
print("\nStudent:", name)
print("Average Score:", round(average, 2))
