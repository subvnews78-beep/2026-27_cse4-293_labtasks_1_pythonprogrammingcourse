# Read marks from the user
marks = int(input("Enter student marks: "))
# Check the grade using elif ladder
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")