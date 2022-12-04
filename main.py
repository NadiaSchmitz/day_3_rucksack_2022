import string

rucksacks = []
first_compartments = []
second_compartments = []
subjects = []
sum = 0

alphabet_low = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
alphabet = alphabet_low + alphabet_upper

with open("rucksack.txt", "r") as file:
    for line in file:
        rucksacks.append(line)
rucksacks[-1] = rucksacks[-1] + "\n"

for item in rucksacks:
    middle_index = round((len(item) - 1) / 2)
    first_compartments.append(item[0:middle_index])
    second_compartments.append(item[middle_index:])

for item in rucksacks:
    middle_index = round((len(item) - 1) / 2)
    check = 0
    for i in range(0, middle_index):
        for j in range(middle_index, len(item)):
            if item[i] == item[j]:
                check = i
    subjects.append(item[check])

for item in subjects:
    sum = sum + (alphabet.index(item) + 1)

print(sum)
