def countdown(n):

    if n <= 0:
        print("Go")
    else:
        print(n)
        countdown(n - 1)

countdown(10)


# same logic written iteratively:

def countdown_itr(n):
    while n > 0:
        print(n)
        n -= 1
    print("GO")

countdown_itr(20)