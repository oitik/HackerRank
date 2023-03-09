import itertools
data = list(input().strip())
it = itertools.groupby(data)
for key, group in it:
    print(f'({len(list(group))}, {int(key)})', end=' ')
# must understand the groupby function.
