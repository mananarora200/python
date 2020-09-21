from stack import Stack


def binary(num):
    rem = ''
    while num!=0:
        if num%2 != 0:
            rem+='1'
        else:
            rem+='0'
        num = num//2
    return rem[::-1]
print(binary(24))
print(binary(2))
print(binary(242))