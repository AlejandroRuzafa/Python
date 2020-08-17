import sys

def mcd (n1,n2):
    while n1 != n2 : 
        if n1 > n2 :
            n1 = n1 - n2
        else : 
            n2 = n2 - n1 

    return n1 
        


def es_primo(n):
    for i in range (2,n):
        if n % i == 0 :
            return False 
    return True    


def first_n_primes(n):
    criba = []
    primo_actual = 1
    while len(criba) < n :
        if es_primo(primo_actual):
            criba.append(primo_actual)
        primo_actual= primo_actual + 1
    return(criba) 


n = int(sys.argv[1])
print(f"Los {n} primeros numeros primos son:")
print(first_n_primes(n))
