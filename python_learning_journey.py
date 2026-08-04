Student_name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Place = input("Enter your place: ")

Python_Mark = int(input("Enter your Python mark: "))
English_Mark = int(input("Enter your English mark: "))
Maths_Mark = int(input("Enter your Maths mark: "))

Total_Mark = Python_Mark + English_Mark + Maths_Mark
Average_Mark = Total_Mark / 3

print("\n========== STUDENT REPORT ==========")
print("Student Name :", Student_name)
print("Age          :", Age)
print("Place        :", Place)

print("\nPython Mark  :", Python_Mark)
print("English Mark :", English_Mark)
print("Maths Mark   :", Maths_Mark)

print("\nTotal Mark   :", Total_Mark)
print("Average Mark :", Average_Mark)
print("====================================")