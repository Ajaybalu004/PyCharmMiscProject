def fibonacci(N,a=0,b=1):
    counter = 0
    while counter < N:
        (a,b ) = (b,a+b)
        print(a,end=" ")
        counter += 1
fibonacci(10)