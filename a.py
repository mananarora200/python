# str1 = 'abcbcsabbbbbbbabadkwsnc'
str1 = 'abskjchbakjdsbcbbbbbbbbbbb'
dict1 = {}
for i in range(len(str1)+1):
    for j in range(i,len(str1)+1):
        if str1[i:j] == str(str1[i:j])[::-1]:
            dict1[len(str1[i:j])]=str1[i:j]
print(dict1[max(dict1)])