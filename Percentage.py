#take marks as input from user
print("Enter the marks obtained in 4 subjects:")
math=int(input("Maths:"))
science=int(input("Science:"))
english=int(input("English:"))
social=int(input("Social:"))
#calculate total marks and percentage
total_marks=math+science+english+social
percentage=(total_marks/400)*100
#print total marks and percentage
print("Total marks obtained:",total_marks)
print("Percentage:",percentage)
