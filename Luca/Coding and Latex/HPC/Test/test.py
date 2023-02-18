import sys

which = int(sys.argv[1])

print(which)

with open(f'data_{which}.txt', 'w') as f:
    f.write(f'This is job number {which}')