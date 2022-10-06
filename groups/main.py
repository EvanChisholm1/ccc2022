x = int(input())
must_map = {}

for i in range(0, x):
    names = input().split()
    if not must_map.get(names[0]):
        must_map[names[0]] = {names[1]: True}
    else:
        must_map[names[0]][names[1]] = True
    if not must_map.get(names[1]):
        must_map[names[1]] = {names[0]: True}
    else:
        must_map[names[1]][names[0]] = True

y = int(input())
forbidden_map = {}

for i in range(0, y):
    names = input().split()
    if not forbidden_map.get(names[0]):
        forbidden_map[names[0]] = {names[1]: True}
    else:
        forbidden_map[names[0]][names[1]] = True
    if not forbidden_map.get(names[1]):
        forbidden_map[names[1]] = {names[0]: True}
    else:
        forbidden_map[names[1]][names[0]] = True

g = int(input())

global violations
violations = 0

for i in range(0, g):
    names = input().split()
    name_map = {}
    for name in names:
        name_map[name] = True
    for name in names:
        othernames = names.copy()
        othernames.remove(name)
        for othername in othernames:
            if forbidden_map.get(name) and forbidden_map[name].get(othername):
                forbidden_map[othername][name] = False
                violations += 1
        
        if must_map.get(name):
            for mustname in must_map[name].keys():
                if mustname not in names and must_map[name][mustname]:
                    must_map[mustname][name] = False
                    violations += 1
        
print(violations)
