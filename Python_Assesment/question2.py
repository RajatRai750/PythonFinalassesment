# Again added the input statement to enter the scores manually in order to get the output back

maths = float(input("Enter the marks of maths: "))
Eng = float(input("Enter the marks of English: "))
phy = float(input("Enter the marks of physics: "))

avg_score = (maths + Eng + phy)/3

if avg_score >= 90:
    grade = "A"
elif 80 <= avg_score < 90:
    grade = "B"
elif 70 <= avg_score < 80:
    grade = "C"
elif 60 <= avg_score < 70:
    grade = "D"
else:
    grade = "F"

print (f"Average Score: {avg_score:.2f}")
print (f"Avg Score: {grade}")