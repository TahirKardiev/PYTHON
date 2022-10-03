n = int(input('Enter number: ')) 

def seq(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(seq(n))
print(round(sum(seq(n))))
