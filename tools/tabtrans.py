while True:
    path = input()
    if len(path) == 0:
        break
    with open(path, 'r') as f:
        data = f.readlines()
        for line in data:
            line.replace('\t', ' ' * 4)
    with open(path, 'w') as f:
        for line in data:
            f.write(line)