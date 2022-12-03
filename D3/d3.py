import string
alphabet = string.ascii_letters

def process(rucksacks):
    priority = ''.join(set(rucksacks[0]).intersection(rucksacks[1]))
    return alphabet.index(priority) + 1

with open("input.txt", "r") as f:
    lst = [el.strip() for el in f.readlines()]
    lst1 = [ [el[:len(el)//2] ,el[len(el)//2:]] for el in lst]
    lst2 = [ [lst[i], ''.join(set(lst[i+1]).intersection(lst[i+2])) ] for i in range(0, len(lst), 3)]
    print(sum(list(map(process, lst1)))) # Part1
    print(sum(list(map(process, lst2)))) # Part2