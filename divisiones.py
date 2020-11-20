import math
def divide2 (numerador, divisor):
  i = 0
  encontrado = False
  while (i<numerador) and encontrado == False:
    act = divisor * i
    sig = divisor * (i+1)
    if (act <= numerador) and (sig >= numerador):
      r = 0
      inicial = act
      while (inicial != numerador)and (r<=divisor):
        inicial += 1
        r += 1
      encontrado = True
      if r == divisor:
        i +=1
        r = 0
    i +=1
  return ((i-1),r)

def divide (dividend, divisor):
  quotient = 0
  while dividend >= divisor:
    dividend -= divisor
    quotient +=1
  return (dividend,quotient)#Estan al reves

def gcd(int1, int2 ):		
		while( int1 != int2 ):
			if( int1 > int2 ):
				int1 -= int2;
			else:
				int2 -= int1
		return int1;


def num_phi(n):
  x=nextPrime(0)
  pi = n
  while x <= n:
    if n%x == 0:
      pi = pi * (1-(1/x))
      print(x,pi)
    x=int(nextPrime(x))
  return pi

def isPrime(n):
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    if(n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False

    return True

def nextPrime(N):
    # Base case
    if (N <= 1):
        return 2
    prime = int(N)
    found = False
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
        if(isPrime(prime) is True):
            found = True
    return int(prime)

#print(num_phi(51))
#print(divide2(x,y))
#print(divide(x,y))
#print(x //y, x%y)
#print(gcd(6,3))
