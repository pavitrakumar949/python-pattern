def tree(n):
    for i in range(n):
        print(" "*(n-i-1) + '*'*(2*i+1))
    for i in range(2):
        print(" "*(n-1)+"*")
tree(7)
