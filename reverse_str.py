from stack import Stack
s1 = Stack()
s = 'manan'
sr = ''
for i in s:
    s1.push(i)
for i in range(len(s)):
    sr+=s1.pop()
print(sr)