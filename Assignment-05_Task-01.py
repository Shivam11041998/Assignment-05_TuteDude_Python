a = {"Shivam": 20, "Rahul": 21, "Raj": 22, "Alice":85, "Bob": 10}
b = input("Enter the student's name: ")
if b in a:
    print(b, " marks's: ",a[b])
else:
    print("Student not found.")


