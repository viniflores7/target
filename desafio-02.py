#Sequência Fibonacci

def fibonacci(n):
    n1 = 0
    n2 = 1
    print(f' {n1} -> {n2}', end='')
    cont=3
    while cont <= n:
        n3 = n1+n2
        print(f' -> {n3}', end='')
        n1=n2
        n2=n3
        cont+=1

print(fibonacci(8))
