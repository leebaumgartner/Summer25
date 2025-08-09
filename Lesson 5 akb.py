
import random

def main():
    print("Welcome to the Grade Calculator!")

    grades = []

    while True:
        grade_input = input("Enter a grade (-1 to finish): ")
        if grade_input == "-1":
            break
        else:
            grades.append(int(grade_input))

    print("\nGrades entered:", grades)

    print("\nRemoving the lowest grade")
    lowest_grade = min(grades)
    lowest_index = grades.index(lowest_grade)
    grades.pop(lowest_index)
    print("Grades after removing the lowest:", grades)

    print("\nRemoving a random grade")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print("Grades after removing random grade:", grades)

    print("\nEditing a grade")
    while True:
        print("Current grades:")
        for i in range(len(grades)):
            print(f"{i+1}: {grades[i]}")  
        choice = int(input("Enter the number of the grade to edit: "))
        if 1 <= choice <= len(grades):
            new_grade = int(input("Enter the new grade: "))
            grades[choice - 1] = new_grade
            break
        else:
            print("Invalid choice. Try again.")

    print("Grades after editing:", grades)

    print("\nSorting and reversing the grades")
    grades.sort()
    grades.reverse()
    print("Grades after sorting and reversing:", grades)

    print("\nCalculating total and average")
    total = sum(grades)
    average = total / len(grades)
    print("Total of grades:", total)
    print("Average grade:", average)


main()
print("This was completed by Annaleigh Baumgartner")