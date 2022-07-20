<<<<<<< HEAD
stu_res = {}

while True:
    name = input('Enter student name: ')
    if name == '':
        break
    mark = int(input("Enter student\'s mark: "))
    if mark not in range(0, 11):
        break

    if name in stu_res:
        stu_res[name] += (mark,)
    else:
        stu_res[name] = (mark,)

for name in sorted(stu_res.keys()):
    total = 0
    count = 0
    for marks in stu_res[name]:
        total += marks
        count += 1

    print(name, ":", total/count)

=======
stu_res = {}

while True:
    name = input('Enter student name: ')
    if name == '':
        break
    mark = int(input("Enter student\'s mark: "))
    if mark not in range(0, 11):
        break

    if name in stu_res:
        stu_res[name] += (mark,)
    else:
        stu_res[name] = (mark,)

for name in sorted(stu_res.keys()):
    total = 0
    count = 0
    for marks in stu_res[name]:
        total += marks
        count += 1

    print(name, ":", total/count)

>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
