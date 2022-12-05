from re import split as multiple_split
stack1 = ''
stack2 = ''

containers, containers2 = [[]] * 9, [[]] * 9
def parse_containers(lst):
    for el in lst:
        for i in range(1, len(el), 4):
            if el[i] != '' and ' ' not in el[i]:
                buffer_containers = containers[(i - 1) // 4].copy()
                buffer_containers.insert(0, el[i])
                containers[(i - 1) // 4] = buffer_containers
                containers2[(i - 1) // 4] = buffer_containers.copy()

def process_inst(inst, order = False):
    n_container = int(inst[0])
    from_container = int(inst[1]) - 1
    to_container = int(inst[2]) - 1
    if order:
        to_remove = containers2[from_container][-n_container:]
        containers2[from_container] = containers2[from_container][:-n_container]
        for crate in to_remove:
            containers2[to_container].append(crate)
        return
    for i in range(0, n_container):
        crate = containers[from_container].pop()
        containers[to_container].append(crate)

with open("input.txt", "r") as f:
    lst = [el.rstrip('\n') for el in f.readlines()]
    lst1 = list(filter(lambda x: '[' and ']' in x, lst))
    parse_containers(lst1)
    lst_moves = list(filter(lambda x: 'move' in x, lst))
    lst_moves = [multiple_split(' from | to ', inst.replace('move ', '')) for inst in lst_moves]
    for inst in lst_moves:
        process_inst(inst)
        process_inst(inst, True)
    for top in range(len(containers)):
        if len(containers[top]) != 0:
            stack1 += containers[top][-1]
            stack2 += containers2[top][-1]
    print('Part1: ', stack1)
    print('Part2: ', stack2)