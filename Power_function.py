
# power function take two parameters a and n
def power(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(3, 2))
