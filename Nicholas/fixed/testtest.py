import sys
import test_2 as g

which = int(sys.argv[1])

print(which)

with open(f'data_{which}.txt', 'w') as f:
    g.write(f'This is not job number {which}')
    
    