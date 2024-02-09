from module5_mod import *

program = find_index()
N = int(input('Please input a positive integer: '))
for i in range(N):
    num = int(input(f'Please input {N} numbers one by one: '))
    program.read_number(num)
X = int(input('Please input a number to search for: '))
ind = program.search(X)
print(ind)