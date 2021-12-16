import time


def howmuchtime(func):
    # les arguments *args, **kwargs permettent d'accepter que la fonction décoré aient touts types et nombres d'arguments
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res

    return wrapper

@howmuchtime
def fib(n):
    print(f"le temps de calcul  de Fibonnaci pour {n} vaut : ")
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a



