<<<<<<< HEAD
input_file = open('words', 'w')

for i in range(3):
    s = input()
    input_file.write(s+"\n")

input_file.close()

input_file = open('words', 'r')
for line in input_file:
    print(line, end='')

input_file.close()
=======
input_file = open('words', 'w')

for i in range(3):
    s = input()
    input_file.write(s+"\n")

input_file.close()

input_file = open('words', 'r')
for line in input_file:
    print(line, end='')

input_file.close()
>>>>>>> 9e3cb6cf133890da221895222230826cf16a1d2f
