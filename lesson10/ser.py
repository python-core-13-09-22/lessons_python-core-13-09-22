from entity import Student, ElectronicChit, PaperChit
import json
students = []
with open("data/students.txt", encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        data = line.split()

        if len(data) == 2:
            student = Student(data[0], data[1])
        if len(data) == 3:
            student.chips.append(ElectronicChit(data[0], int(data[1]), data[2]))
        if len(data) == 4:
            student.chips.append(PaperChit(data[0], int(data[1]), int(data[2]), data[3]))
        if len(data) == 0:
            students.append(student)



# data = json.dumps(students, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# with open("data/input.json", mode="w") as file:
#     file.write(data)

with open("data/input.json", mode="r") as file:
    data = json.load(file)

print(data)