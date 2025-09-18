print("Hello, we want to calculate the rate")

number_Materials = int(input("Enter number 'at least 3': "))
sum = 0
for i in range(1, number_Materials + 1):
    grade = float(input(f"Enter grade course {i}: "))
    sum += grade  
avg = sum / number_Materials

if avg >= 85:
    evaluation = "Excellent"
elif avg >= 70:
    evaluation = "Very Good"
elif avg >= 50:
    evaluation = "Good"
else:
    evaluation = "Fail"   

print("avg:", avg)           
print("Evaluation:", evaluation) 
 

