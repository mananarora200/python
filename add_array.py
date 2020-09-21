a = [[1,2,3],[4,5,6]]
b = [[1,2,3],[4,5,6]]
c = []
for i in range(len(a)):
    temp = []
    for j in range(len(a[0])):
        temp.append(a[i][j]+b[i][j])
    c.append(temp)
print(c)
        