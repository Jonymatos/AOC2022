def verify1(pair):
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or\
        (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])

def verify2(pair):
    return (pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]) or\
        (pair[0][0] >= pair[1][1] and pair[0][1] <= pair[1][0])

with open("input.txt", "r") as f:
    lst = [el.strip().split(',') for el in f.readlines()]
    lst = list(map(lambda x: [list(map(int, x[0].split('-'))), list(map(int, x[1].split('-')))], lst))
    print(len(list(filter(verify1, lst))))
    print(len(list(filter(verify2, lst))))
    