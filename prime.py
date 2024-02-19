def is_prime(number):
    if number <= 1:
        return False
    
    if number % 2 == 0 or number % 3 == 0:
        return False 
    for i in range(5, int(number**0.5) + 1, 6):
        if number% i == 0 or number % (i + 2) == 0:
            return False
    return True
number =57
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


