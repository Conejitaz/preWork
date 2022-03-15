def factorial(n):
    """Calcula el factorial de n
    n int > 0
    returns n!
    """
    ##print(n) par saber que esta factorizando
    if n == 1:
        return  1
    return n * factorial(n - 1)
n = int(input('numero: '))
print(factorial(n))