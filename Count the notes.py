#Taking total amount as input from user
total_amount=int(input("Enter the total amount:"))
#Calculating the number of notes with different denominations
note_1=total_amount//100
note_2=(total_amount%100)//50
note_3=((total_amount%100)%50)//10
print("number of 100 rupee notes is:",note_1)
print("number of 50 rupee notes is:",note_2)
print("number of 10 rupee notes is:",note_3)