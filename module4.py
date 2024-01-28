
N = int(input('Please input a positive integer: '))
numbers = []
for i in range(N):
    numbers.append(int(input(f'Please input {N} numbers one by one: ')))

X = int(input('Please input a number to search for: '))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)