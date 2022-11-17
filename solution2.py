# Write code for algorithm 2 below
def count_up(n,i):
    if n>i:
        return
    else:
        print(n)
        count_up(n+1,i)

count_up(1,8)