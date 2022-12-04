def verify1(pair):
    return (int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1])) or\
        (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]))

def verify2(pair):
    return (int(pair[0][0]) <= int(pair[1][1]) and int(pair[0][1]) >= int(pair[1][0])) or\
        (int(pair[0][0]) >= int(pair[1][1]) and int(pair[0][1]) <= int(pair[1][0]))  

with open("input.txt", "r") as f:
    lst = [el.strip().split(',') for el in f.readlines()]
    lst = list(map(lambda x: [x[0].split('-'), x[1].split('-')], lst))
    print(len(list(filter(verify1, lst))))
    print(len(list(filter(verify2, lst))))
    