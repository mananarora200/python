import itertools
a = [1,2,3,4,5]
b = 'manan'
iter_a = []
iter_b = []
iter_a2 = []
iter_b2 = []
for i in itertools.combinations(a,2):
    iter_a.append(i)
print(iter_a)
for i in itertools.combinations(b,2):
    iter_b.append(''.join(i))
print(iter_b)
for i in itertools.permutations(a):
    iter_a2.append(i)
print(iter_a2)
for j in range(len(b)+1):    
    for i in itertools.combinations(b,j):
        if ''.join(i)!='':
            iter_b2.append(''.join(i))
print(iter_b2)