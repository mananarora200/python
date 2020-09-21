a1 = [[1,2],[3,4]]
a2 = [[5,6],[7,8]]
a3 = []
for i in range(len(a1)):
    temp = []
    sum = 0
    for j in range(i,len(a1[0])):
        for k in range(j,len(a1[0])):
            sum+=a1[j][k]*a2[k][j]
        temp.append(sum)
    a3.append(temp)
print(a3)
