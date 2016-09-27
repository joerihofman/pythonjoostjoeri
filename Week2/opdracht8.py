#Een perfect getal is een positief geheel getal dat de som is al van zijn eigen delers. Bijvoorbeeld 6 = 3 + 2 + 1 en
#daarom een perfect getal. En 28 is ook een perfect getal. Schrijf een programma dat de 4 perfecte getallen vindt
#onder de 10.000.
n = 1
lim = 10000
while n<lim:
    factors = [1]
    [factors.append(i) for i in range(2,n+1) if n%i == 0]
    if sum(factors) == 2*n: print(n)
    n += 1

#result: 6, 28, 496, 8128