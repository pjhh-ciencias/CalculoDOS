a0=int(input('Ingresa la aproximación inicial: '))
n=10
A=20
for i in range(1,101):
    an=0.5*(a0 + A/a0)
    print('a',i,'=',an)
    a0=an
