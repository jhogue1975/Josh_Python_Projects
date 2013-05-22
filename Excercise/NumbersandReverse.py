open_file = open('Excercise3.txt')
open_file.close

line_split = []
for line in open_file:
    line_split.append(line)

    for item in line_split:
        sum_of_numbers = []
        for number in item:
            if number.isdigit():
                sum_of_numbers.append(int(number))

    for line in line_split:
        no_happy = []
        for word in line.split():
            if word.lower() != "happy":
                no_happy.append(word)

            print no_happy
