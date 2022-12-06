with open("day1.txt", "r") as file:
    input = file.read()

input = max([sum([int(n) for n in x.split("\n")]) for x in input.strip().split("\n\n")])
print(input)
