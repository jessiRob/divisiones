def divide (numerador, divisor):
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

def mcd (num1,num2):
  a = num1
  b = num2
  divisores = []
  div = 1
  while (a > 1) and (b > 1) and (div <= num1) and (div <= num2):
    a,r1 = divide(a,div)
    b,r2 = divide(b,div)
    print(div, a,r1,b,r2)
    if (a == b) and (r1 == 0) and (r2 == 0):
      divisores.append(div)
      print(divisores)
      div = 1
    div +=1
    print(div)
    print((a > 1) and (b > 1))
  divisores.sort()
  return divisores[0]

lt = [1,2]
print (lt[-1])

x = 2
y = 6
print(divide(x,y))
print(x //y, x%y)
print(mcd(6,3))
