input_file = open('words', 'w')

for i in range(3):
    s = input()
    input_file.write(s+"\n")

input_file.close()

input_file = open('words', 'r')
for line in input_file:
    print(line, end='')

input_file.close()
