def read_h(file='kmeans.txt'):
    lines = open(file, "r").read().split('\n')
    attribs = lines[0].split(' ')
    instances = []
    for i in range(1, len(lines)):
        instances.append(lines[i].split(' '))
    return attribs

