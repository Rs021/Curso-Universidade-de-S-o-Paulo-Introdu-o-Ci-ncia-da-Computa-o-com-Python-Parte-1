file = open('teste.txt')

for line in file:
    line.rstrip()
    if line.startswith('From:'):
        print(line)