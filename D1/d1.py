buffer = []
total = []
with open("input.txt", "r") as f:
    lst = [el.strip() for el in f.readlines()]
    for num in lst:
        if num == "":
            total.append(sum(buffer))
            buffer = []
        else:
            buffer.append(int(num))

# Write "1" for Part1 and "3" for Part2
top = int(eval(input("Enter the top number: ")))
print(sum(sorted(total, reverse = True)[:top]))