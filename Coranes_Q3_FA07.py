students = []
for i in range(3):
    print(f"Student {i + 1}")
    s = {}
    s["name"] = input("Enter name: ")
    s["age"] = int(input("Enter age: "))
    s["grade"] = input("Enter grade: ")
    students.append(s)

print("Class Directory:")
for s in students:
    print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")