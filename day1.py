with open("day1.txt", "r") as file:
    input = file.read()

# part one
most = max([sum([int(n) for n in x.split("\n")]) for x in input.strip().split("\n\n")])
print(most)

# part two

top_three = [sum([int(n) for n in x.split("\n")]) for x in input.strip().split("\n\n")]
top_three.sort(reverse=True)
top_three = top_three[0] + top_three[1] + top_three[2]
print(top_three)
