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

x = 100
y = 2
print(divide2(x,y))
print(divide(x,y))
print(x //y, x%y)
print(gcd(6,3))
