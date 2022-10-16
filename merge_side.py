

import sys

paths = sys.argv[1:]

contents = []

for p in paths:
    with open(p, 'r') as f:
        for i, line in enumerate(f):
            if len(contents) > i:
                ci = contents[i]
            else:
                ci = ''
            ci += line.strip()
            if len(contents) > i:
                contents[i] = ci
            else:
                contents.append(ci)

w = len(contents[1])
h = len(contents)
print(f'{w} {h - 1}')

for line in contents[1:]:
    print(line)