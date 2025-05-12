password = input('Enter password:')
if password == '123456':
    print('Correct password')
else:
    print('Incorrect password')

num = input('Enter a number:')
name = input('Enter your name:')
print((name + '\n') * int(num))

posi = input('Enter a positive integer:')
if int(posi) > 0:
    for i in range(int(posi), 1001, int(posi)):
        print(i)
else:
    posi = input('Enter a positive integer:')

n = input('Enter a integer:')
if int(n) <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    import math
    for i in range(2, int(math.sqrt(int(n))) + 1):
        if int(n) % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number.")
    else:                                           
        print(f"{n} is not a prime number.")

for m in range(1,101):
    result = ''
    if m % 3 == 0:
        result += 'Fizz'
    if m % 5 == 0:
        result += 'Buzz'
    print(result or m)
