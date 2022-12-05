from re import split as multiple_split

containers, containers2 = [[]] * 9, [[]] * 9
def parse_containers(lst):
    for el in lst:
        for i in range(1, len(el), 4):
            if el[i] != '' and ' ' not in el[i]:
                buffer_containers = containers[(i - 1) // 4].copy()
                buffer_containers.insert(0, el[i])
                containers[(i - 1) // 4] = buffer_containers
                containers2[(i - 1) // 4] = buffer_containers.copy()

def process_inst(inst, cont, same_order = False):
    n_container, from_container, to_container = int(inst[0]), int(inst[1]) - 1, int(inst[2]) - 1
    to_add = cont[from_container][-n_container:]
    cont[from_container] = cont[from_container][:-n_container]

    if not same_order: to_add.reverse()
    for crate in to_add: cont[to_container].append(crate)

with open("input.txt", "r") as f:
    lst = [el.rstrip('\n') for el in f.readlines()]
    parse_containers( list(filter(lambda x: '[' and ']' in x, lst)) )
    lst_moves = list(filter(lambda x: 'move' in x, lst))
    lst_moves = [multiple_split(' from | to ', inst.replace('move ', '')) for inst in lst_moves]

    for inst in lst_moves:
        process_inst(inst, containers)
        process_inst(inst, containers2, True)

    stack1 = ''.join([stack[-1] for stack in containers if len(stack) != 0]) #Part1: SVFDLGLWV
    stack2 = ''.join([stack[-1] for stack in containers2 if len(stack) != 0]) #Part2: DCVTCVPCL
    print(f"Part1: {stack1}\nPart2: {stack2}")