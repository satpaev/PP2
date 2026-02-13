def valid(n):
    v = True
    while n != 0:
        a = n % 10
        if a % 2 == 0:
            n //= 10
        else:
            v = False
            break
    if v:
        print("Valid")
    else:
        print("Not valid")

m = int(input())
valid(m)