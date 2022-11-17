# Write code for algorithm 3 below
def Fibbonacci(n):
    if n<=1:
        return n
    else:
        
        return (Fibbonacci(n-1)+Fibbonacci(n-2))

print(Fibbonacci(8))